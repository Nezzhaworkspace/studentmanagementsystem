import { useState } from "react";
import api from "./api";

function Delete() {

  const [roll, setRoll] = useState("");


  async function handleDelete(e) {

    e.preventDefault();

    const confirmDelete = window.confirm(
      `Are you sure you want to delete student ${roll}?`
    );

    if (!confirmDelete) {
      return;
    }


    try {

      const response = await api.delete(`/delet/${roll}`);

      console.log(response.data);

      alert("Student Deleted Successfully!");

      setRoll("");

    } catch (error) {

      console.log(error);

      alert("Unable to delete student");

    }

  }


  return (
    <div className="page-container delete-page">

      <h1>Delete Student</h1>

      <form onSubmit={handleDelete}>

        <div>

          <label>Enter Roll Number</label>

          <input
            type="number"
            value={roll}
            onChange={(e) => setRoll(e.target.value)}
            placeholder="Enter roll number"
            required
          />

        </div>


        <button
          type="submit"
          className="delete-btn"
        >
          Delete Student
        </button>

      </form>

    </div>
  );
}

export default Delete;

