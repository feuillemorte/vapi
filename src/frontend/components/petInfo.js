import styles from "../styles/petInfo.module.css";

import Card from 'react-bootstrap/Card'
import Button from 'react-bootstrap/Button';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { useContext } from "react";
import navValues from "@/helpers/petNavValues";
import { navigationContext } from "@/pages/pets";

const PetInfo = () => {
    const { param: pet, navigate } = useContext(navigationContext);
    return (
        <Card className={styles.card}>
            <Row>
                <Col>
                    <Card.Img src={pet.img_url} />
                </Col>
                <Col>
                    <Card.Body className={styles.cardBody}>
                        <Card.Title className={styles.cardTitle}>{pet.name}</Card.Title>
                        <Card.Text className={styles.cardText}>{pet.description}</Card.Text>
                        <Button className={styles.cardDetails} onClick={() => navigate(navValues.pets)}>Back</Button>
                    </Card.Body>
                </Col>
            </Row>
        </Card>
    );
};

export default PetInfo;
