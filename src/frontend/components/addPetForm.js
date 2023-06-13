import styles from "styles/addPetForm.module.css"

import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { useState } from "react";

import usePets from "@/hooks/usePets";

const AddPetForm = () => {
    const default_pet_state = {name: "", description: "", img_url: "/img/pets/default.jpeg"}
    const [ pet, setPet ] = useState(default_pet_state);
    const change = ((event) => setPet({...pet, [event.target.name]: event.target.value}))
    const { pets, setPets, addPet } = usePets();
    const submit = (event) => {
        event.preventDefault();
        addPet(pet);
        setPet(default_pet_state);
    }

    return (
        <>
            <h1 className={styles.title}>Add a new pet</h1>
            <Form onSubmit={submit} className={styles.form}>
                <Form.Group>
                    <Form.Label className={styles.label}>Name</Form.Label>
                    <Form.Control className={styles.input} type="text" name="name" placeholder="Enter the pet name" value={pet.name}
                    onChange={change}/>
                </Form.Group>

                <Form.Group>
                    <Form.Label className={styles.label}>Description</Form.Label>
                    <Form.Control className={styles.input} as="textarea" rows={10} type="text" name="description" placeholder="Enter the pet description" value={pet.description}
                    onChange={change} />
                </Form.Group>

                <Form.Group>
                    <Form.Label className={styles.label}>Pet photo</Form.Label>
                    <Form.Control className={styles.input} type="file" name="img_url" />
                </Form.Group>

                <Button className={styles.submit} type="submit">
                    Submit
                </Button>
            </Form>
        </>
    );
}

export default AddPetForm;
