const firstNameElement = document.getElementById("first-name");
const lastNameElement = document.getElementById("last-name");
const emailElement = document.getElementById("email");
const passwordElement = document.getElementById("password");
const confirmPasswordElement = document.getElementById("confirm-password");
const errorElement = document.querySelector(".error-message");
const submitButton = document.querySelector(".submit-button");
const form = document.querySelector("form");

const url = "http://localhost:3000/login";

const handleSignUp = async (e) => {
  e.preventDefault();
  const firstName = firstNameElement.value;
  const lastName = lastNameElement.value;
  const email = emailElement.value;
  const password = passwordElement.value;
  const confirmPassword = confirmPasswordElement.value;

  errorElement.innerHTML = "";

  if (password.length < 8)
    return (errorElement.innerText =
      "Password must have at least 8 characters");
  if (password !== confirmPassword)
    return (errorElement.innerText = "Password and confirm must match");

  try {
    const response = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        firstName,
        lastName,
        email,
        password,
      }),
    });
    if (!response.ok) throw new Error("Failed to sign up");
    const result = await response.json();
    console.log(result);
    submitButton.innerText = "Account creation succesful";
  } catch (err) {
    console.error(err.message);
  }
};

form.addEventListener("submit", handleSignUp);
