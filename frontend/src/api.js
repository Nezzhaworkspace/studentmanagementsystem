import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "https://smsystem-y3an.onrender.com",
});

export default api;