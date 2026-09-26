import { useEffect, useState } from "react";
import api from "./api";

function Allstudents() {

  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let isMounted = true;

    api.get("/studentslist")
      .then((response) => {
        if (isMounted) {
          setStudents(response.data);
        }
      })
      .catch((error) => {
        if (isMounted) {
          const detail = error.response?.data?.detail;
          alert(detail || "Unable to fetch students");
        }
      })
      .finally(() => {
        if (isMounted) {
          setLoading(false);
        }
      });

    return () => {
      isMounted = false;
    };
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

