import { FormErrorMessage, useColorModeValue, Input, Box, Button, FormControl, Modal, ModalBody, ModalCloseButton, ModalContent, ModalHeader, ModalOverlay, useDisclosure, useToast, Textarea, FormLabel, Switch, ModalFooter, Stack } from "@chakra-ui/react"
import { useParams } from "react-router-dom";
import { useForm, Controller } from "react-hook-form"

export const AddUpdateToDoModal = ({
    editable=false,
    defaultValues={},
    onSuccess = () => {},
    ...rest
}) => {
    const { isOpen, onOpen, onClose} = useDisclosure();
    const toast = useToast();
    const { todoId } = useParams();
    const { handleSubmit, register, control, formState: {
        errors, isSubmitting
    } } = useForm({
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
                            <FormControl isInvalid={errors.title}>
                                <Input
                                placeholder="ToDo Title..."
                                background={useColorModeValue('gray.300', 'gray.600')}
                                type="text"
                                variant="filled"
                                size="lg"
                                mt={6}
                                {...register("title", {
                                    required: "This is a required field",
                                    minLength: {
                                        value: 5,
                                        message: "Title must be at least 5 characters"
                                    },
                                    maxLength: {
                                        value: 55,
                                        message: "Title must be at most 55 characters"
                                    }
                                })}
                                />
                                <FormErrorMessage>
                                    {errors.title && errors.title.message}
                                </FormErrorMessage>
                            </FormControl>
                            <FormControl isInvalid={errors.title}>
                                <Textarea
                                row={5}
                                placeholder="Add Description..."
                                background={useColorModeValue('gray.300', 'gray.600')}
                                type="text"
                                variant="filled"
                                size="lg"
                                mt={6}
                                {...register("description", {
                                    required: "This is a required field",
                                    minLength: {
                                        value: 5,
                                        message: "Description must be at least 5 characters"
                                    },
                                    maxLength: {
                                        value: 200,
                                        message: "Description must be at most 200 characters"
                                    }
                                })}
                                />
                                <FormErrorMessage>
                                    {errors.description && errors.description.message}
                                </FormErrorMessage>
                            </FormControl>
                            <Controller
                            control={control}
                            name= "status"
                            render={({field}) => (
                                <FormControl mt={6} display="flex" alignItems="center">
                                    <FormLabel htmlFor="is-done"> Status </FormLabel>
                                    <Switch
                                        onChange={(e) => field.onChange(e.target.checked)}
                                        isChecked={field.value}
                                        id="id-done"
                                        size="lg"
                                        name="status"
                                        idDisabled={false}
                                        colorScheme="green"
                                        variant="ghost"
                                    />
                                </FormControl>
                            )}
                            />
                        </ModalBody>
                        <ModalFooter>
                            <Stack direction="row" spacing={4}>
                                <Button 
                                onClick={onClose}
                                disabled={isSubmitting}>
                                    Close
                                </Button>
                                <Button 
                                colorScheme="green"
                                type="submit"
                                isLoading={isSubmitting}
                                loadingText={editable ? "Updating" : "Creating"}
                                >
                                    {editable ? "Update" : "Create"}
                                </Button>
                            </Stack>
                        </ModalFooter>
                    </ModalContent>
                </form>
            </Modal>
        </Box>    
    );
}