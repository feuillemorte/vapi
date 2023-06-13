import styles from "../styles/navBar.module.css";

import { Nav } from "react-bootstrap";

const NavBar = () => {
    return (
        <Nav id={styles.navBar}>
            <Nav.Link href="/" className={styles.link}>Home</Nav.Link>
            <Nav.Link href="/pets" className={styles.link}>Pets</Nav.Link>
            <Nav.Link href="/about" className={styles.link}>About us</Nav.Link>
            <Nav.Link href="/404" className={styles.link}>404</Nav.Link>
            <Nav.Link href="/admin" className={styles.link}>Admin</Nav.Link>
        </Nav>
    );
};

export default NavBar;
