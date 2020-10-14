var selectedItems = {};
var prices = {};

fetch("./api/v1/getItemList")
  .then(function (response) {
    if (response.status !== 200) {
      console.log("Failed to fetch items");
      return;
    }

    response.json().then(function (data) {
      var items = document.getElementById("items");

      data.forEach(renderItem);

      function renderItem(detail) {
        let item = document.createElement("div");
        item.className = "item";

        let imagePath = "static/" + detail["fields"]["image_path"];
        let stocks = detail["fields"]["quantity"];
        let name = detail["fields"]["name"];
        let price = detail["fields"]["price"];
        let id = detail["pk"];

        prices[id] = price;

        let html = `<div class="buttons">
                                </div>
                                <div class="image">
                                <img src="${imagePath}" alt="" width=120 height=80/>
                                </div>

                                <div class="description">
                                <span>${name}</span>
                                <span>Available stocks: ${stocks}</span>
                                </div>

                                <div class="quantity">
                                <button class="plus-btn" type="button" name="button">
                                    <img src="static/plus.svg" alt="" />
                                </button>
                                <input type="text" id="${id}" value="0">
                                <button class="minus-btn" type="button" name="button">
                                    <img src="static/minus.svg" alt="" />
                                </button>
                                </div>

                                <div class="total-price">$${price}</div>`;

        item.innerHTML = html;
        items.appendChild(item);
      }

      $(".minus-btn").on("click", function (e) {
        e.preventDefault();
        var $this = $(this);
        var $input = $this.closest("div").find("input");
        var value = parseInt($input.val());

        if (value > 1) {
          value = value - 1;
        } else {
          value = 0;
        }

        $input.val(value);

        selectedItems[$input.attr("id")] = value;
      });

      $(".plus-btn").on("click", function (e) {
        e.preventDefault();
        var $this = $(this);
        var $input = $this.closest("div").find("input");
        var value = parseInt($input.val());

        if (value < 100) {
          value = value + 1;
        } else {
          value = 100;
        }

        $input.val(value);

        selectedItems[$input.attr("id")] = value;
      });

      $(".btn").on("click", function (e) {
        e.preventDefault();

        let payload = {};
        payload["selectedItems"] = [];

        for (let [key, value] of Object.entries(selectedItems)) {
          if (value > 0) {
            let item = { pk: key, price: prices[key], quantity: value };
            payload["selectedItems"].push(item);
          }
        }

        fetch("./api/v1/getState", {
          method: "post",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(payload),
        }).then(function (response) {
          if (response.status !== 200) {
            console.log("Failed to get state");
            return;
          }

          response.json().then(function (data) {
            console.log(data);
            if ("error" in data) {
              alert(data["error"]);
              return;
            }
            window.location.href =
              "checkout?state=" + encodeURIComponent(data["state"]);
          });
        });
      });
    });
  })
  .catch(function (err) {
    console.log("Fetch Error :", err);
  });
