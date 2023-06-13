import styles from "../styles/banner.module.css";
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Container from 'react-bootstrap/Container';

const Banner = () => {
    return (
        <Container id={styles.container} fluid={true}>
            <Row>
                <div id={styles.header}>
                    <p>VAPI</p>
                    <p>Pet Care</p>
                </div>
            </Row>
            <Row>
                <div id={styles.title}>
                    <p>We&apos;ll care for your pets</p>
                    <p >the same way you do.</p>
                </div>
            </Row>
            <Row>
                <Col id={styles.buttonContainer}>
                    <Button  href="/pets">Learn more</Button>
                </Col>
            </Row>
        </Container>
    );
};

export default Banner;
