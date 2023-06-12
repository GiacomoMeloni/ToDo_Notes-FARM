import { useState, useRef, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom"; 
import AxiosInstance from "../../services/auth_service";
import { Button, Center, Container, Spinner } from "@chakra-ui/react"

export const ToDoDetail = () => {
    const [todo, setTodo] = useState({});
    const [loading, setLoading] = useState(true);
    const isMounted = useRef(false);
    const navigate = useNavigate();
    const { todoId } = useParams()

    useEffect(() => {
        if (isMounted.current) return;
        fetchTodo();
        isMounted.current = true;
    }, [todoId]);

    const fetchTodo = () => {
        setLoading(true)
        AxiosInstance.get(`/todo/${todoId}`)
        .then((response) => {
            setTodo(response.data)
        })
        .catch((error) => console.error(error))
        .finally(() => {
            setLoading(false);
        })
    }

    if (loading) {
        return (
            <Container mt={6}>
                <Center mt={6}>
                    <Spinner
                        thickness="4px"
                        speed="0.65s"
                        emptyColor="green.200"
                        color="green.500"
                        size="xl"
                    />
                </Center>
            </Container>
            
        )
    }
    
    return (
        <>
            <Container mt={6}>
                <Button 
                colorScheme="gray"
                onClick={() => navigate('/', {replace: true})}>
                    Back
                </Button>
            </Container>
        </>
    );
}