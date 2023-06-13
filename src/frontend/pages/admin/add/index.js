import { Container } from "react-bootstrap";
import NavBar from "@/components/navBar";
import AddPetForm from "@/components/addPetForm";


function AddPet() {
    return (
        <Container fluid={true}>
            <NavBar />
            <AddPetForm />
        </Container>
    );
}

export default AddPet;
