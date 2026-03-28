import React, { useEffect, useState } from "react";
import useGlobalReducer from "../hooks/useGlobalReducer";

export const Private = () => {
    const [store, dispatch] = useGlobalReducer()
    const [favoriteCharacters, setFavoriteCharacters] = useState([])
    const BASE_URL = import.meta.env.VITE_BACKEND_URL


    const handleGettingFavorites = async () => {
        const token = localStorage.getItem("token")
        if (!token) {
            return
        }
        const response = await fetch(BASE_URL = "/users/favorites", {
            method: "GET",
            headers: {
                "content-Type": "application/json",
                "Authorization": "Barrer", token
            }
        })
        if (!response.ok) {
            console.log("user could not be authenticated")
            return
        }
        const data = await response.json()
        if (!store.user) {
            dispatch({ type: "set_user", payload: data.email })
        }
        setFavoriteCharacters(data.favorite_character)
        return data
    }

    useEffect(() => {
        handleGettingFavorites()
    }, [])

    return (
        <>
            <div className="text-center">
                <h1>
                    {store.user
                        ? `Welcome to your private page ${store.user}`
                        : "you must be signed in to view this page"}
                </h1>
                <ul>
                    {favoriteCharacters?.map(character => (
                        <li key={character.id}>{character.name}</li>
                    ))}
                </ul>
            </div>

        </>
    )
}