import { createContext, useEffect, useReducer, useRef } from "react"
import { validateToken } from "../utils/jwt";
import { setSession } from "../utils/session";

const initialState = {
    isAuthenticated: false,
    isInitialize: false,
    user: null
}

export const AuthContext = createContext({
    ...initialState,
    login: () => Promise.resolve(),
    logout: () => Promise.resolve(),
});

const handlers = {
    INITIALIZE: (state, action) => {
        const { isAuthenticated, user} = action.payload; 
        
        return {
            ...state,
            isAuthenticated,
            isInitialize: true,
            user: user
        };
    },

    LOGIN: (state, action) => {
        const {user} = action.payload;

        return {
            ...state,
            isAuthenticated: true,
            user: user
        };
    },

    LOGOUT: (state, action) => {
        return {
            ...state,
            isAuthenticated: false,
            user: null
        };
    }
}


const reducer = (state, action) => handlers[action.type] ? handlers[action.type](state, action) : state;

const AuthProvider = (props) => {
    const {children} = props;
    const [state, dispatch] = useReducer(reducer, initialState)
    const isMouted = useRef(false)

    useEffect(() => {
        if (isMouted.current) return;

        const initialize = async () => {
            try {
                const accessToken = localStorage.getItem("accessToken")
                if (accessToken && validateToken(accessToken)){
                     setSession(accessToken)
                     const response = await AxiosInstance.get("/users/me");
                     const {data: user} = response;
                     dispatch({
                        type: "INITIALIZE",
                        payload: {
                            isAuthenticated: true,
                            user
                        }
                     });
                } else {
                    dispatch({
                        type: "INITIALIZE",
                        payload: {
                            isAuthenticated: false,
                            user: null
                        }
                    });
                }
            }catch (error){
                console.error(error);
                
                dispatch({
                    type: "INITIALIZE",
                    payload: {
                        isAuthenticated: false,
                        user: null
                    }
                });
            }
        }
        initialize(); 
        isMouted.current = true;
    }, []);   
} 
