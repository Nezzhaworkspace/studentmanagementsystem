import { useEffect, useState } from "react";
import api from "./api";

function Allstudents() {

  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);

  async function getStudents() {

    try {

      const response = await api.get("/studentslist");

      console.log(response.data);

      setStudents(response.data);

    } catch (error) {

      console.log(error);

      alert("Unable to fetch students");

    } finally {

      setLoading(false);

    }

  }

  useEffect(() => {

    getStudents();

  }, []);


  if (loading) {
    return <h2>Loading students...</h2>;
  }


  return (
    <div className="page-container">

      <h1>All Students</h1>

      <div className="table-container">

        <table>

          <thead>

            <tr>
              <th>Roll Number</th>
              <th>Name</th>
              <th>Age</th>
              <th>Email</th>
            </tr>

          </thead>


          <tbody>

            {students.length === 0 ? (

              <tr>
                <td colSpan="4">
                  No students found
                </td>
              </tr>

            ) : (

              students.map((student) => (

                <tr key={student.roll}>

                  <td>{student.roll}</td>

                  <td>{student.name}</td>

                  <td>{student.age}</td>

                  <td>{student.email}</td>

                </tr>

              ))

            )}

          </tbody>

        </table>

      </div>

    </div>
  );
}

export default Allstudents;

