import { useState, useRef, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom"; 
import AxiosInstance from "../../services/auth_service";
import { Text, Button, Center, Container, Spinner, useColorModeValue } from "@chakra-ui/react"
import { AddUpdateToDoModal } from "./AddUpdateToDoModal";

export const ToDoDetail = () => {
    const [todo, setTodo] = useState({});
    const [loading, setLoading] = useState(true);
    const isMounted = useRef(false);
    const navigate = useNavigate();
    const { todoId } = useParams()
    const background = useColorModeValue("gray.300", "gray.600");

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
            <Container
            bg={background}
            minHeight="7rem"
            my={3}
            p={3}
            rounded="lg"
            alignItems="center"
            justifyContent="space-between">
                <Text fontSize={22}> {todo.title} </Text>
                <Text bg="gray.500" mt={2} p={2} rounded="lg"> {todo.description} </Text>
                <AddUpdateToDoModal
                    my={3}
                    editable={true}
                    defaultValues={{
                        title: todo.title, 
                        description: todo.description, 
                        status: todo.status
                    }}
                    onSuccess={fetchTodo} 
                />
            </Container>
        </>
    );
}