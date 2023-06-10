import { useEffect, useRef, useState } from "react";
import { Box, Center, Container, Spinner } from "@chakra-ui/react"
import AxiosInstance from "../../services/auth_service";

export const ToDoList = () => {
    const [todos, setTodos] = useState([]);
    const [loading, setLoading] = useState(true);
    const isMounted = useRef(false);
    
    useEffect(() => {
        if (isMounted) return;
        fetchToDo();
        isMounted.current = true;
    }, []);

    const fetchToDo = async () => {
        setLoading(true);
        AxiosInstance.get("/todo")
        .then((res) => {
            setTodos(res.data);
        }).catch((error) => {
            console.error(error);
        }).finally(() => {
            setLoading(false);
        });
    }
    
    return (
        <Container mt={9}>
            {loading ? (
                <Center mt={6}>
                    <Spinner
                        thickness="4px"
                        speed="0.65s"
                        emptyColor="green.200"
                        color="green.500"
                        size="xl"
                    />
                </Center>
            ) : ( 
                <Box mt={6}>
                    { todos?.map((todo) => (
                        <TodoCard todo={todo} key={todo.id}/>
                    ))}
                </Box>
            )}
             {/* Add ToDo modal  */}
        </Container>
    );
}