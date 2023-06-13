import { useEffect, useState } from "react";
import useGetRequest from "./useGetRequest";


const usePets = () => {
    const [pets, setPets] = useState([]);
    const get = useGetRequest("/api/pets")

    useEffect(() => {
        const fetchPets = async () => {
            const pets = await get();
            setPets(pets);
        };
        fetchPets();
    }, [get]);

    const postPet = async (pet) => {
        await fetch("/api/pets", {
            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-type": "application/json",
            },
            body: JSON.stringify(pet),
        });
    };

    const addPet = (pet) => {
        postPet(pet);
        setPets([...pets, pet]);
    }

    return { pets, setPets, addPet };
};

export default usePets;
