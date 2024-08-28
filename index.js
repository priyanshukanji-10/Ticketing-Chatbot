const express = require("express");
const PORT = 8000;

const app = express();

app
  .route("/login")
  .get((req, res) => {
    res.json({ status: "Pending" });
  })
  .patch((req, res) => {
    res.json({ status: "Pending" });
  });

app
  .route("/signup")
  .get((req, res) => {
    res.json({ status: "Pending" });
  })
  .patch((req, res) => {
    res.json({ status: "Pending" });
  });

app.listen(PORT, () => {
  console.log(`Server started at: ${PORT}`);
});
