import styles from "styles/petList.module.css";

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

import PetCard from "./petCard";
import usePets from "@/hooks/usePets";

const PetList = () => {
    const { pets, setPets, addPet } = usePets();

    return (
        <Container>
            <Row>
                <Col><h1 className={styles.title}>Our pets</h1></Col>
            </Row>
            <Row>
                {pets.map((pet) => (
                    <Col key={pet.id}>
                        <PetCard pet={pet}/>
                    </Col>
                ))}
            </Row>
        </Container>
    );
};

export default PetList;
