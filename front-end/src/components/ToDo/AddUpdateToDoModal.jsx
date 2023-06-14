import { Box, Button, FormControl, Modal, ModalBody, ModalCloseButton, ModalContent, ModalHeader, ModalOverlay, useDisclosure, useToast } from "@chakra-ui/react"
import { useParams } from "react-router-dom";
import { useForm } from "react-hook-form;"

export const AddUpdateToDoModal = ({
    editable=false,
    defaultValues={},
    onSuccess = () => {},
    ...rest
}) => {
    const { isOpen, onOpen, onClose} = useDisclosure();
    const toast = useToast();
    const { todoId } = useParams();
    const { handleSubmit, register, control } = useForm({
        defaultValues: {...defaultValues}
    });

    return (
        <Box {...rest}>
            <Button w="100%" colorScheme="green" onClick={onOpen}>
                {editable ? "Update ToDo" : "Add ToDo"}
            </Button>
            <Modal 
            closeOnOverlayClick={false}
            size="xl"
            onClose={onClose}
            isOpen={isOpen}
            isCentered
            >
                <ModalOverlay/>
                <form>
                    <ModalContent>
                        <ModalHeader>
                            {editable ? "Update ToDo" : "Add ToDo"}
                        </ModalHeader>
                        <ModalCloseButton/>
                        <ModalBody>
                            <FormControl></FormControl>
                        </ModalBody>
                    </ModalContent>
                </form>
            </Modal>
        </Box>    
    );
}