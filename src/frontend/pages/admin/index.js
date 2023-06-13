import styles from "styles/adminPanel.module.css"

import { Button, Col, Container, Row } from "react-bootstrap";
import NavBar from "@/components/navBar";

const AdminPanel = () => {
    return (
        <Container fluid={true}>
            <NavBar />
            <Row>
                <Col><h1 className={styles.title}>Admin Panel</h1></Col>
            </Row>
            <Row>
                <Col><Button href="/admin/add" className={styles.addPetButton}>Add a pet</Button></Col>
            </Row>
        </Container>
    );
};

export default AdminPanel;
