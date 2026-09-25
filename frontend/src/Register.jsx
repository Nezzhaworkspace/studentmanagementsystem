import { useState } from "react";
import api from "./api";

function Register() {

  const [roll, setRoll] = useState("");
  const [name, setName] = useState("");
  const [age, setAge] = useState("");
  const [email, setEmail] = useState("");

  async function handleSubmit(e) {

    e.preventDefault();

    try {

      const response = await api.post("/createStudent", {
        roll: Number(roll),
        name: name,
        age: Number(age),
        email: email
      });

      console.log(response.data);

      alert("Student Registered Successfully!");

      // Clear form

      setRoll("");
      setName("");
      setAge("");
      setEmail("");

    } catch (error) {

      console.log(error);

      alert("Something went wrong!");

    }

  }

  return (
    <div className="page-container">

      <h1>Register Student</h1>

      <form onSubmit={handleSubmit}>

        <div>
          <label>Roll Number</label>

          <input
            type="number"
            value={roll}
            onChange={(e) => setRoll(e.target.value)}
            placeholder="Enter roll number"
            required
          />
        </div>


        <div>
          <label>Name</label>

          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="Enter student name"
            required
          />
        </div>


        <div>
          <label>Age</label>

          <input
            type="number"
            value={age}
            onChange={(e) => setAge(e.target.value)}
            placeholder="Enter age"
            required
          />
        </div>


        <div>
          <label>Email</label>

          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter email"
            required
          />
        </div>


        <button type="submit">
          Register Student
        </button>

      </form>

    </div>
  );
}

export default Register;

