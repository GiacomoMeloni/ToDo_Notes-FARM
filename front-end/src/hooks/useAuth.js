import { useContext } from "react";
import { AuthContext } from "../context/jwtAuthContext";

export const useAuth = () => useContext(AuthContext);