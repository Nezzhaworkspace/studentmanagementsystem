import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav>

      <h2>Student Management System</h2>

      <div>

        <Link to="/">Home</Link>

        <Link to="/register">Register</Link>

        <Link to="/allstudents">All Students</Link>

        <Link to="/update">Update</Link>

        <Link to="/delete">Delete</Link>

      </div>

    </nav>
  );
}

export default Navbar;