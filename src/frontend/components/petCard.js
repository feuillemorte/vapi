import styles from "../styles/petCard.module.css";

import Card from 'react-bootstrap/Card'
import Button from 'react-bootstrap/Button';
import { useContext } from "react";
import navValues from "@/helpers/petNavValues";
import { navigationContext } from "@/pages/pets";

const PetCard = ({ pet }) => {
    const { navigate } = useContext(navigationContext);
    return (
        <Card className={styles.card}>
            <Card.Img className={styles.cardImage} variant="top" src={pet.img_url} />
            <Card.Body className={styles.cardBody}>
                <Card.Title className={styles.cardTitle}>{pet.name}</Card.Title>
                <Button className={styles.cardDetails} onClick={() => navigate(navValues.petInfo, pet)}>Details</Button>
            </Card.Body>
        </Card>
    );
}

export default PetCard;
