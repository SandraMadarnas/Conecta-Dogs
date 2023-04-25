# VOLVER AL ULTIMO COMMIT
git reset --hard

# INSTALAR FLASK+JWT 
pipenv install flask-jwt-extended

# INSTALAR DATEPICKER
npm install react-datepicker --save

import React, { useState } from "react";
import DatePicker from "react-datepicker";

import "react-datepicker/dist/react-datepicker.css";

// CSS Modules, react-datepicker-cssmodules.css
// import 'react-datepicker/dist/react-datepicker-cssmodules.css';

<!-- const Example = () => {
  const [startDate, setStartDate] = useState(new Date());
  return (
    <DatePicker selected={startDate} onChange={(date) => setStartDate(date)} />
  );
}; -->

# COPIAR CARPETA DE OTRA RAMA
git checkout NOMBRERAMA carpeta/

# RESETEAR BASE DE DATOS
rm -R -f ./migrations &&
pipenv run init &&
psql -U gitpod -c 'DROP DATABASE example;' || true &&
psql -U gitpod -c 'CREATE DATABASE example;' &&
psql -U gitpod -c 'CREATE EXTENSION unaccent;' -d example &&
pipenv run migrate &&
pipenv run upgrade

MEJOR --> pipenv run reset_db

# UPGRADE DB
pipenv run upgrade

<!-- ********************** -->
# INSTALAR REACT SCROLL
Inicio rápido: Usar react-scroll
Creará una aplicación sencilla en este tutorial, pero si desea un resumen rápido de cómo funciona react-scroll, consulte estos pasos resumidos:

Instale react-scroll:

npm i -S react-scroll
Importe el paquete react-scroll:

import { Link, animateScroll as scroll } from "react-scroll";
Añada el componente de enlace. El componente <Link /> apuntará a un área concreta de su aplicación:

<Link to="section1">