const url = window.location.origin;

document.getElementById("unlock-box").addEventListener(
    "click",
    async () => {
        const dialog = document.getElementById("dialog-dark");
        const datas = await fetch(`${url}/show`, {
            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name: document.getElementById("box-name").value,
                secret: document.getElementById("box-secret").value,
            }),
        });

        const boxs = await datas.json();
        dialog.getElementsByClassName("content")[0].innerHTML = boxs.datas
            ? boxs.datas.content
            : "Your f**king secret key is wrong bruhh !!";
        dialog.showModal();
    },
    false,
);
