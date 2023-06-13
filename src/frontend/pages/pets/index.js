import PetComponentPicker from "@/components/petComponentPicker";
import NavBar from "@/components/navBar";
import petNavValues from "@/helpers/petNavValues";
import React, { useCallback, useState } from 'react';

const navigationContext = React.createContext(petNavValues.pets)

const Pets = () => {
    const navigate = useCallback(
        (navTo, param) => setNav({current: navTo, param, navigate}),
        []
    );
    const [nav, setNav] = useState({current: petNavValues.pets, navigate});

    return (
        <div>
            <NavBar />
            <navigationContext.Provider value={nav}>
                <PetComponentPicker currentNavLocation={nav.current} />
            </navigationContext.Provider>
        </div>
    );
}

export { navigationContext };
export default Pets;
