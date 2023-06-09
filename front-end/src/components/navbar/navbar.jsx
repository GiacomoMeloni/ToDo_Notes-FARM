import { useColorModeValue, Box, Flex, Text, Stack, Button } from "@chakra-ui/react"
import { ThemeToggler } from "../theme/themeToggler"
import { Outlet } from "react-router-dom";
import { useAuth } from "../../hooks/useAuth";

export const NavBar = () => {

    const { logout } = useAuth();

    return (
        <Box min height="100vh">
            <Flex
            as="nav"
            alignItems="center"
            justify="space-between"
            wrap="wrap"
            padding="1rem"
            bg={useColorModeValue("green.300", "green.600")}
            color="white">
                <Text as="h2" fontSize={24} fontWeight="bold"> 
                    {" "}
                    TODO LIST 
                </Text>

                <Stack direction="row" align="center" spacing={4}>
                    <ThemeToggler size="lg"/>
                    <Button onClick={logout} colorScheme="green">Logout</Button>
                </Stack>
            </Flex>
            <Outlet />
        </Box>
    )
}