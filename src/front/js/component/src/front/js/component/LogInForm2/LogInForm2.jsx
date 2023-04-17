import React from "react";
import "../LogInForm2/login-form2.css";
import "../LogInForm2/login_form2.js";

const LogInForm2 = () => {
    return (
        <>
            <div className="row">
                <div className="container">
                    {/* <div className="col-12 col-md-4"></div> */}

                    <div className="col-12 col-md-6">
                        <div class="background">
                            <form class="login-form">
                                <h3>Iniciar Sesión</h3>

                                <label for="username">Usuario</label>
                                <input type="text" placeholder="Correo Electrónico" id="username" />

                                <label for="password">Contraseña</label>
                                <input type="password" placeholder="Contraseña" id="password" />

                                <button>Iniciar Sesión</button>

                                <div className="p-2">
                                    <a href="">
                                        <i class="far fa-question-circle"></i>
                                        ¿Olvidaste tu contraseña?
                                    </a>
                                </div>


                                <div class="social">
                                    <div class="go"><i class="fab fa-google"></i>  Google</div>
                                    <div class="fb"><i class="fab fa-facebook-f"></i>  Facebook</div>
                                </div>
                            </form>
                        </div>
                    </div>

                    <div className="col-12 col-md-6">
                        <div class="background">
                            <form class="login-form">
                                <h3>Registro de Usuario</h3>

                                <div className="form-group glowing-register-wrapper">
                                    <div className="glowing-register m-2">
                                        <input type="radio" id="propietario" name="perfil" value="propietario" />
                                        <label for="propietario">Propietario</label>
                                    </div>
                                    <div className="glowing-register m-2">
                                        <input type="radio" id="cuidador" name="perfil" value="cuidador" />
                                        <label for="cuidador">Cuidador</label>
                                    </div>
                                </div>

                                <label for="name">Nombre</label>
                                <input type="text" placeholder="Nombre" id="username" />

                                <label for="apellidos">Apellidos</label>
                                <input type="text" placeholder="Apellidos" id="username" />

                                <label for="username">Usuario</label>
                                <input type="text" placeholder="Correo Electrónico" id="username" />

                                <label for="password">Contraseña</label>
                                <input type="password" placeholder="Contraseña" id="password" />

                                <button>Registrarse</button>

                                <div class="social">
                                    <div class="go"><i class="fab fa-google"></i>  Google</div>
                                    <div class="fb"><i class="fab fa-facebook-f"></i>  Facebook</div>
                                </div>
                            </form>
                        </div>
                    </div>

                </div>
            </div>

        </>
    );
};

export default LogInForm2;
