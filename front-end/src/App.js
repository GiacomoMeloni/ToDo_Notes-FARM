import {BrowserRouter as Router, Routes, Route, Navigate} from 'react-router-dom'
import { Login } from './components/auth/login';
import { Register } from './components/auth/register'
import { AuthProvider, AuthConsumer } from './context/jwtAuthContext';
import { Flex, Spinner } from '@chakra-ui/react';

function App() {
  return (
    <AuthProvider>
    <Router>
      <AuthConsumer>
        {(auth) => !auth.isInitialized ? (
          <Flex
          height="100vh"
          alignItems="center"
          justifyContent="center"
          >
            <Spinner
            thickness="4xp"
            speed="0.65s"
            emptyColor="green.200"
            color="green.500"
            size="xl"
            >

            </Spinner>
          </Flex>
        ) : (
        <Routes>
          <Route path="/login" element={<h1><Login/></h1>} />
          <Route path="/register" element={<h1><Register/></h1>} />
          <Route path="/" element={<h1>I am home</h1>} />
          <Route path="*" element={<Navigate to="/"/>}/>
        </Routes>
      )}
      </AuthConsumer>
    </Router>
    </AuthProvider>
  )
}

export default App;
