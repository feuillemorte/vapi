import styles from "styles/about.module.css"

import { Card, Col, Container, Row } from "react-bootstrap";
import NavBar from "@/components/navBar";

const About = () => {
    const description = "VAPI is a vulnerable application which contains different sort of vulnerabilities. This application is designed to be a test application for different scanners and manual observation. \n \n Stay secure!"
    const signature = "VAPI team"
    return (
        <Container fluid={true}>
            <NavBar />
            <Card>
                <Row>
                    <Col>
                        <Card.Body className={styles.cardBody}>
                            <Card.Title className={styles.cardTitle}>About us</Card.Title>
                            <Card.Text className={styles.cardText}>{description}</Card.Text>
                            <Card.Text className={styles.cardSignature}>{signature}</Card.Text>
                        </Card.Body>
                    </Col>
                    <Col>
                        <Card.Img src="/img/about.jpeg" />
                    </Col>
                </Row>
            </Card>
        </Container>
    );
};

export default About;
