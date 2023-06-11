import { Badge, Flex, useColorModeValue, Text } from "@chakra-ui/react"

export const ToDoCard = ( {todo} ) => {
    return (
        <Flex
        bg={useColorModeValue("gray.300", "gray.600")}
        minHeight="3rem"
        my={3}
        p={3}
        rounded="lg"
        alignItems="center"
        justifyContent="space-between"
        _hover={{
            opacity: 0.9,
            cursor: "pointer",
            transform: "translateY(-3px)"
        }}
        >
            <Text> {todo.title} </Text>
            <Badge colorScheme={todo.status ? "green" : "purple"}>
                {todo.status ? "Completed" : "Pending"}
            </Badge>
        </Flex>
    );
}