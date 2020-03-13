/**
 * ArkavPay Core Service
 * Balance route
 * 
 * Copyright (c) ArkavPay. Proprietary and confidential.
 * 
 * @author patriot
 */
import { Request, Response, Router } from 'express';
import { getUser, deductBalance, deductCoins, increaseBalance, increaseCoins } from "../model/user";
import { checkUserAgentSecure } from "../helper/fraudservice";

const router = Router();

router.get('/check', async (request: Request, reply: Response) => {
  const authUser = request.user;

  if (!authUser) {
    reply.status(401).send({error: "Unauthorized"});
    return;
  }

  const user = await getUser(authUser.username);
  reply.send({ balance: user.balance, arkavCoins: user.arkavCoins });
});

router.post('/arkavcoins/topup', async (request: Request, reply: Response) => {
  const authUser = request.user;

  if (!authUser) {
    reply.status(401).send({error: "Unauthorized"});
    return;
  }

  const nominal = parseInt(request.body.nominal);

  if (Number.isNaN(nominal)) {
    reply.status(401).send({error: "Nominal should be an integer"});
    return;
  }

  if (nominal <= 0) {
    reply.status(401).send({error: "Nominal must be positive"});
    return;
  }

  const user = await getUser(authUser.username);

  if (user.balance < nominal) {
    reply.status(400).send({error: "Insufficient funds"});
    return;
  }

  // Check for fraud
  const isSecure = await checkUserAgentSecure(request.ip);

  if (!isSecure) {
    reply.status(403).send({error: "Our fraud analytics service detected anomaly."});
    return;
  }

  // All is well, let's top it up
  await deductBalance(authUser.id, nominal);
  const newUser = await increaseCoins(authUser.id, nominal);

  reply.send({ ...newUser, password: undefined });
});

router.post('/arkavcoins/refund', async (request: Request, reply: Response) => {
  const authUser = request.user;

  if (!authUser) {
    reply.status(401).send({error: "Unauthorized"});
    return;
  }

  const nominal = parseInt(request.body.nominal);

  if (Number.isNaN(nominal)) {
    reply.status(401).send({error: "Nominal should be an integer"});
    return;
  }

  if (nominal <= 0) {
    reply.status(401).send({error: "Nominal must be positive"});
    return;
  }

  const user = await getUser(authUser.username);

  if (user.arkavCoins < nominal) {
    reply.status(400).send({error: "Insufficient coins"});
    return;
  }

  // Check for fraud
  const isSecure = await checkUserAgentSecure(request.ip);

  if (!isSecure) {
    reply.status(403).send({error: "Our fraud analytics service detected anomaly."});
    return;
  }

  // All is well, let's top it up
  await increaseBalance(authUser.id, nominal);
  const newUser = await deductCoins(authUser.id, nominal);

  reply.send({ ...newUser, password: undefined });
});

export default router;
