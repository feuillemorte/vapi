import navValues from "@/helpers/petNavValues";
import PetList from "./petList";
import PetInfo from "./petInfo";

const PetComponentPicker = ({ currentNavLocation }) => {
    switch (currentNavLocation) {
        case navValues.pets:
            return <PetList />;
        case navValues.petInfo:
            return <PetInfo />;
        default:
            return (
                <h3>No component for navigation {currentNavLocation} value found</h3>
            );
    }
};

export default PetComponentPicker;
