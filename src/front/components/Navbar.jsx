import { Link } from "react-router-dom";
import storeReducer from "../store";
import { StoreProvider } from "../hooks/useGlobalReducer";

export const Navbar = () => {

	return (
		<nav className="navbar navbar-light bg-light">
			<div className="container">
				<Link to="/">
					<span className="navbar-brand mb-0 h1">React Boilerplate</span>
				</Link>
				<div className="ml-auto">
					<Link>
						<div>
							{
								store.user ?
									<button className="btn btn-primary">Sign out</button>
									:
									<div>
										<link to="/Signup">
											<button className="btn btn-primary">Sign up</button>
										</link>
										<link to="/LogIn">
											<button className="btn btn-primary">Log In</button>
										</link>
										<link to="/Private">
											<button className="btn btn-primary">Private</button>
										</link>
									</div>
							}
						</div>
					</Link>
				</div>
			</div>
		</nav>
	);
};