import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Navigate } from "react-router-dom";


export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="text-center mt-5">
			{
				store.token ?
					<h1>Tienes acceso</h1> :
					<Navigate to={"/login"} />
			}
		</div>
	);
};
