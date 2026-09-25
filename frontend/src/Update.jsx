import { useState } from "react";
import api from "./api";

function Update() {

  const [roll, setRoll] = useState("");
  const [name, setName] = useState("");
  const [age, setAge] = useState("");
  const [email, setEmail] = useState("");


  async function handleUpdate(e) {

    e.preventDefault();

    try {

      // Create object for update
      const updateData = {};

      // Add only fields which are entered
      if (name.trim() !== "") {
        updateData.name = name;
      }

      if (age !== "") {
        updateData.age = Number(age);
      }

      if (email.trim() !== "") {
        updateData.email = email;
      }


      // Check if user entered at least one field
      if (Object.keys(updateData).length === 0) {

        alert("Please enter at least one field to update");
        return;

      }


      const response = await api.put(`/edit/${roll}`, updateData);


      console.log(response.data);


      if (response.data.message === "Student updated successfully") {

        alert("Student Updated Successfully!");

        // Clear form
        setRoll("");
        setName("");
        setAge("");
        setEmail("");

      } else {

        alert("Student Updated Successfully!");

      }


    } catch (error) {

      console.log(error);

      alert("Unable to update student");

    }

  }


  return (
    <div className="page-container">

      <h1>Update Student</h1>


      <form onSubmit={handleUpdate}>

        {/* Roll Number */}

        <div className="update-roll">

          <label>Enter Roll Number</label>

          <input
            type="number"
            value={roll}
            onChange={(e) => setRoll(e.target.value)}
            placeholder="Enter roll number"
            required
          />

        </div>


        {/* Name */}

        <div>

          <label>New Name</label>

          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="Enter new name"
          />

        </div>


        {/* Age */}

        <div>

          <label>New Age</label>

          <input
            type="number"
            value={age}
            onChange={(e) => setAge(e.target.value)}
            placeholder="Enter new age"
          />

        </div>


        {/* Email */}

        <div>

          <label>New Email</label>

          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter new email"
          />

        </div>


        <button type="submit">
          Update Student
        </button>

      </form>

    </div>
  );
}

export default Update;