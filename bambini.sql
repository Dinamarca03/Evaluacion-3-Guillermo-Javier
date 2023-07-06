-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-07-2023 a las 00:46:20
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bambini`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add Producto', 7, 'add_producto'),
(26, 'Can change Producto', 7, 'change_producto'),
(27, 'Can delete Producto', 7, 'delete_producto'),
(28, 'Can view Producto', 7, 'view_producto'),
(29, 'Can add Devolucion', 8, 'add_devolucion'),
(30, 'Can change Devolucion', 8, 'change_devolucion'),
(31, 'Can delete Devolucion', 8, 'delete_devolucion'),
(32, 'Can view Devolucion', 8, 'view_devolucion'),
(33, 'Can add Sucursal', 9, 'add_sucursal'),
(34, 'Can change Sucursal', 9, 'change_sucursal'),
(35, 'Can delete Sucursal', 9, 'delete_sucursal'),
(36, 'Can view Sucursal', 9, 'view_sucursal'),
(37, 'Can add rol', 10, 'add_rol'),
(38, 'Can change rol', 10, 'change_rol'),
(39, 'Can delete rol', 10, 'delete_rol'),
(40, 'Can view rol', 10, 'view_rol'),
(41, 'Can add Salida', 11, 'add_ingresarsalidaproductos'),
(42, 'Can change Salida', 11, 'change_ingresarsalidaproductos'),
(43, 'Can delete Salida', 11, 'delete_ingresarsalidaproductos'),
(44, 'Can view Salida', 11, 'view_ingresarsalidaproductos'),
(45, 'Can add stock', 12, 'add_stock'),
(46, 'Can change stock', 12, 'change_stock'),
(47, 'Can delete stock', 12, 'delete_stock'),
(48, 'Can view stock', 12, 'view_stock'),
(49, 'Can add nombre producto', 13, 'add_nombreproducto'),
(50, 'Can change nombre producto', 13, 'change_nombreproducto'),
(51, 'Can delete nombre producto', 13, 'delete_nombreproducto'),
(52, 'Can view nombre producto', 13, 'view_nombreproducto'),
(53, 'Can add Entrada', 14, 'add_ingresarentradaproductos'),
(54, 'Can change Entrada', 14, 'change_ingresarentradaproductos'),
(55, 'Can delete Entrada', 14, 'delete_ingresarentradaproductos'),
(56, 'Can view Entrada', 14, 'view_ingresarentradaproductos'),
(57, 'Can add categoria', 15, 'add_categoria'),
(58, 'Can change categoria', 15, 'change_categoria'),
(59, 'Can delete categoria', 15, 'delete_categoria'),
(60, 'Can view categoria', 15, 'view_categoria');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$390000$MsImUMLBpSRvyIHjJWgSbn$baUV2pz75o+cnOk0je48FpgsdTgS5TiK4NHJx9jD+6E=', '2023-07-06 20:26:53.529732', 1, 'javier', '', '', '', 1, 1, '2023-07-06 20:26:29.569746'),
(2, 'pbkdf2_sha256$390000$jlHgZQ2YYFUEYrzdFp3qNO$3gaa73nQVOTgtB4zMhOoOvoR1Abhhq2MvJQoXLClm60=', '2023-07-06 22:30:40.776620', 0, 'javierdinamarcaxd@gmail.com', 'Javier2', 'Dinamarca2', '', 0, 1, '2023-07-06 20:27:10.000000'),
(3, 'pbkdf2_sha256$390000$dBdSpEUCGTinIhYvw6nbBE$NLH7Ol/8XMm4IHE0czqXShSWxccDEiEcL7EF9GFowAQ=', '2023-07-06 20:53:04.692973', 0, 'smpegazoz@hotmail.com', 'memo', 'mwmo1', '', 0, 1, '2023-07-06 20:52:03.568287'),
(4, 'pbkdf2_sha256$390000$uwr6kMapMviXBnkVjCmwSm$4Lb7Py/QHccyxtDEhTllDTwdkRpYvHzYLrSgPaTO7yo=', '2023-07-06 22:30:57.694731', 0, 'c@gmail.com', 'c', 'c', '', 0, 1, '2023-07-06 21:27:40.116409');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-07-06 20:27:11.119509', '2', 'javierdinamarcaxd@gmail.com', 1, '[{\"added\": {}}]', 4, 1),
(2, '2023-07-06 20:27:17.245898', '2', 'javierdinamarcaxd@gmail.com', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]', 4, 1),
(3, '2023-07-06 20:27:25.732282', '2', 'javierdinamarcaxd@gmail.com', 2, '[{\"changed\": {\"fields\": [\"Rol\"]}}]', 10, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(15, 'moduloApp', 'categoria'),
(8, 'moduloApp', 'devolucion'),
(14, 'moduloApp', 'ingresarentradaproductos'),
(11, 'moduloApp', 'ingresarsalidaproductos'),
(13, 'moduloApp', 'nombreproducto'),
(7, 'moduloApp', 'producto'),
(10, 'moduloApp', 'rol'),
(12, 'moduloApp', 'stock'),
(9, 'moduloApp', 'sucursal'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-07-06 20:26:01.058638'),
(2, 'auth', '0001_initial', '2023-07-06 20:26:01.430736'),
(3, 'admin', '0001_initial', '2023-07-06 20:26:01.518756'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-07-06 20:26:01.526759'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-07-06 20:26:01.534770'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-07-06 20:26:01.590785'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-07-06 20:26:01.610782'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-07-06 20:26:01.626794'),
(9, 'auth', '0004_alter_user_username_opts', '2023-07-06 20:26:01.630788'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-07-06 20:26:01.670798'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-07-06 20:26:01.674799'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-07-06 20:26:01.682801'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-07-06 20:26:01.698806'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-07-06 20:26:01.714807'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-07-06 20:26:01.730811'),
(16, 'auth', '0011_update_proxy_permissions', '2023-07-06 20:26:01.742816'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-07-06 20:26:01.758825'),
(18, 'moduloApp', '0001_initial', '2023-07-06 20:26:01.778826'),
(19, 'moduloApp', '0002_rename_productos_producto', '2023-07-06 20:26:01.790837'),
(20, 'moduloApp', '0003_devolucion', '2023-07-06 20:26:01.810834'),
(21, 'moduloApp', '0004_sucursal', '2023-07-06 20:26:01.830837'),
(22, 'moduloApp', '0005_rol', '2023-07-06 20:26:01.886852'),
(23, 'moduloApp', '0006_alter_producto_options_alter_sucursal_options_and_more', '2023-07-06 20:26:01.982886'),
(24, 'moduloApp', '0007_rename_id_sucursal_sucursal_nombre', '2023-07-06 20:26:01.994881'),
(25, 'moduloApp', '0008_alter_devolucion_nombre_producto', '2023-07-06 20:26:02.078902'),
(26, 'moduloApp', '0009_remove_sucursal_nombre_sucursal_sucursal_id_sucursal_and_more', '2023-07-06 20:26:02.811093'),
(27, 'moduloApp', '0010_ingresarsalidaproductos', '2023-07-06 20:26:02.835099'),
(28, 'moduloApp', '0011_alter_ingresarsalidaproductos_options', '2023-07-06 20:26:02.839104'),
(29, 'moduloApp', '0012_alter_ingresarsalidaproductos_options', '2023-07-06 20:26:02.839104'),
(30, 'moduloApp', '0013_stock', '2023-07-06 20:26:02.859106'),
(31, 'moduloApp', '0014_stock_id_producto_stock', '2023-07-06 20:26:02.883112'),
(32, 'moduloApp', '0015_nombreproducto', '2023-07-06 20:26:02.903123'),
(33, 'moduloApp', '0016_alter_nombreproducto_id_producto_and_more', '2023-07-06 20:26:02.927124'),
(34, 'moduloApp', '0017_rename_nombreproducto_nombreproducto_nombre_producto', '2023-07-06 20:26:02.939126'),
(35, 'moduloApp', '0018_alter_producto_nombre', '2023-07-06 20:26:03.031150'),
(36, 'moduloApp', '0019_alter_ingresarsalidaproductos_options_and_more', '2023-07-06 20:26:03.043155'),
(37, 'moduloApp', '0020_alter_devolucion_fecha', '2023-07-06 20:26:03.079162'),
(38, 'moduloApp', '0021_alter_devolucion_fecha', '2023-07-06 20:26:03.115172'),
(39, 'moduloApp', '0022_user', '2023-07-06 20:26:03.135178'),
(40, 'moduloApp', '0023_usuario_delete_user', '2023-07-06 20:26:03.159183'),
(41, 'moduloApp', '0024_delete_usuario', '2023-07-06 20:26:03.167186'),
(42, 'moduloApp', '0025_usuario', '2023-07-06 20:26:03.243205'),
(43, 'moduloApp', '0026_user_producto_fecha_delete_usuario', '2023-07-06 20:26:03.291218'),
(44, 'moduloApp', '0027_remove_devolucion_hora_ingresarsalidaproductos_fecha_and_more', '2023-07-06 20:26:03.359236'),
(45, 'moduloApp', '0028_alter_devolucion_options', '2023-07-06 20:26:03.363236'),
(46, 'moduloApp', '0029_devolucion_hora_alter_devolucion_fecha', '2023-07-06 20:26:03.415250'),
(47, 'moduloApp', '0030_remove_devolucion_hora_alter_devolucion_fecha', '2023-07-06 20:26:03.463264'),
(48, 'moduloApp', '0031_remove_stock_motivo', '2023-07-06 20:26:03.475266'),
(49, 'moduloApp', '0032_ingresarsalidaproductos_hora_producto_hora_and_more', '2023-07-06 20:26:03.571290'),
(50, 'moduloApp', '0033_devolucion_hora_alter_devolucion_fecha', '2023-07-06 20:26:03.627306'),
(51, 'moduloApp', '0034_alter_devolucion_nombre_producto', '2023-07-06 20:26:03.791348'),
(52, 'moduloApp', '0035_ingresarsalidaproductos_cantidad_comprada', '2023-07-06 20:26:03.815364'),
(53, 'moduloApp', '0036_ingresarsalidaproductos_accion', '2023-07-06 20:26:03.835361'),
(54, 'moduloApp', '0037_ingresarentradaproductos', '2023-07-06 20:26:03.855366'),
(55, 'moduloApp', '0038_categoria', '2023-07-06 20:26:03.875370'),
(56, 'moduloApp', '0039_alter_producto_tipo_producto', '2023-07-06 20:26:03.983401'),
(57, 'moduloApp', '0040_rename_nombre_producto_devolucion_id_venta', '2023-07-06 20:26:04.127446'),
(58, 'moduloApp', '0041_devolucion_nombre_producto_devolucion_tipo_producto', '2023-07-06 20:26:04.171450'),
(59, 'moduloApp', '0042_remove_devolucion_nombre_producto_and_more', '2023-07-06 20:26:04.195458'),
(60, 'moduloApp', '0043_devolucion_nombre_producto', '2023-07-06 20:26:04.215463'),
(61, 'moduloApp', '0044_remove_devolucion_nombre_producto', '2023-07-06 20:26:04.231470'),
(62, 'moduloApp', '0045_alter_producto_nombre', '2023-07-06 20:26:04.431527'),
(63, 'moduloApp', '0046_producto_id_producto_alter_producto_nombre', '2023-07-06 20:26:04.635568'),
(64, 'moduloApp', '0047_usuario_delete_user', '2023-07-06 20:26:04.663576'),
(65, 'moduloApp', '0048_delete_usuario', '2023-07-06 20:26:04.671578'),
(66, 'moduloApp', '0049_devolucion_nombre_producto', '2023-07-06 20:26:04.691583'),
(67, 'moduloApp', '0050_remove_devolucion_nombre_producto_and_more', '2023-07-06 20:26:04.727594'),
(68, 'moduloApp', '0051_devolucion_nombre_producto', '2023-07-06 20:26:04.747597'),
(69, 'moduloApp', '0052_ingresarentradaproductos_id_producto', '2023-07-06 20:26:04.771604'),
(70, 'moduloApp', '0053_devolucion_id_producto', '2023-07-06 20:26:04.791617'),
(71, 'sessions', '0001_initial', '2023-07-06 20:26:04.819617');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('adr3k6i4jtvlyzgdlaisw2cab4o5rdnk', '.eJxVjDsOwyAQBe9CHSFrWWzsMn3OgBZYYvKBCOwqyt1jSy6S9s28eQtL6zLbtXG1KYhJoDj9bo78nfMOwo3ytUhf8lKTk7siD9rkpQR-nA_3LzBTm7e3GoADoO8HQKO9VqgVoebo0XVj7F00HQLzEIA7Go3yvTGkECiOCoLboq-anlzJNm6pZDEtdeXPF_SqP_c:1qHWVw:x7hlnuZDg9iFoS3_u6I8ojo5dO9XQPtKdXI5aGkKxqs', '2023-07-20 21:27:48.321512'),
('tl6hnra86dhlnrybayajcb5qfzykvugr', '.eJxVjDsOwjAQBe_iGllO_GGTkp4zWLvxhpiPjWynQtwdIqWA9s28eQmPa1v8Wrn4GMQoenH43QinG6cNhCumS5ZTTq1Ekpsid1rlOQe-n3b3L7BgXbZ3IMegHQ0KXQfAgbuZnNazDmBmpa0zBNhZ6g2AUQADwKSc1WiPCvAbfZb44IK-co05ibGVld8f_Mo_cg:1qHW2k:WFQbwF6anGSGPLTFl1gxPXXLW_6WO_UuhNbAuuypY0M', '2023-07-20 20:57:38.718656');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `moduloapp_categoria`
--

CREATE TABLE `moduloapp_categoria` (
  `id` bigint(20) NOT NULL,
  `nombre_categoria` varchar(100) NOT NULL,
  `id_categoria` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `moduloapp_categoria`
--

INSERT INTO `moduloapp_categoria` (`id`, `nombre_categoria`, `id_categoria`) VALUES
(2, '2', '2');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `moduloapp_devolucion`
--

CREATE TABLE `moduloapp_devolucion` (
  `id` bigint(20) NOT NULL,
  `id_venta_id` bigint(20) NOT NULL,
  `fecha` date NOT NULL,
  `cantidad` int(11) NOT NULL,
  `hora` time(6) NOT NULL,
  `nombre_producto` varchar(100) NOT NULL,
  `id_producto` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `moduloapp_devolucion`
--

INSERT INTO `moduloapp_devolucion` (`id`, `id_venta_id`, `fecha`, `cantidad`, `hora`, `nombre_producto`, `id_producto`) VALUES
(1, 2, '2023-07-06', 5, '16:48:07.018457', 'Papasfritas', 'P_1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `moduloapp_ingresarentradaproductos`
--

CREATE TABLE `moduloapp_ingresarentradaproductos` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `tipo_producto` varchar(50) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `hora` time(6) NOT NULL,
  `cantidad_comprada` int(10) UNSIGNED NOT NULL CHECK (`cantidad_comprada` >= 0),
  `accion` varchar(100) NOT NULL,
  `id_producto` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `moduloapp_ingresarentradaproductos`
--

INSERT INTO `moduloapp_ingresarentradaproductos` (`id`, `nombre`, `tipo_producto`, `cantidad`, `fecha`, `hora`, `cantidad_comprada`, `accion`, `id_producto`) VALUES
(1, 'hamburguesas', 'COMIDA', 110, '2023-07-06', '16:43:47.961635', 10, 'agregar', 'H_1'),
(2, 'Papasfritas', 'COMIDA', 105, '2023-07-06', '16:46:25.534853', 5, 'agregar', 'P_1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `moduloapp_ingresarsalidaproductos`
--

CREATE TABLE `moduloapp_ingresarsalidaproductos` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `tipo_producto` varchar(50) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `hora` time(6) NOT NULL,
  `cantidad_comprada` int(10) UNSIGNED NOT NULL CHECK (`cantidad_comprada` >= 0),
  `accion` varchar(100) NOT NULL,
  `id_producto` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `moduloapp_ingresarsalidaproductos`
--

INSERT INTO `moduloapp_ingresarsalidaproductos` (`id`, `nombre`, `tipo_producto`, `cantidad`, `fecha`, `hora`, `cantidad_comprada`, `accion`, `id_producto`) VALUES
(1, 'hamburguesas', 'COMIDA', 105, '2023-07-06', '16:44:00.265327', 5, 'descontar', 'H_1'),
(2, 'Papasfritas', 'COMIDA', 90, '2023-07-06', '16:46:33.455929', 15, 'descontar', 'P_1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `moduloapp_nombreproducto`
--

CREATE TABLE `moduloapp_nombreproducto` (
  `id` bigint(20) NOT NULL,
  `nombre_producto` varchar(100) NOT NULL,
  `id_producto` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `moduloapp_nombreproducto`
--

INSERT INTO `moduloapp_nombreproducto` (`id`, `nombre_producto`, `id_producto`) VALUES
(3, 'A', 'M'),
(4, 'b', 'b');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `moduloapp_producto`
--

CREATE TABLE `moduloapp_producto` (
  `id` bigint(20) NOT NULL,
  `nombre_id` bigint(20) NOT NULL,
  `tipo_producto_id` bigint(20) NOT NULL,
  `valor_unitario` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `sucursal_id` bigint(20) NOT NULL,
  `fecha` date NOT NULL,
  `hora` time(6) NOT NULL,
  `id_producto` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `moduloapp_rol`
--

CREATE TABLE `moduloapp_rol` (
  `id` bigint(20) NOT NULL,
  `rol` varchar(2) NOT NULL,
  `usuario_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `moduloapp_rol`
--

INSERT INTO `moduloapp_rol` (`id`, `rol`, `usuario_id`) VALUES
(1, 'US', 1),
(2, 'AD', 2),
(3, 'US', 3),
(5, 'US', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `moduloapp_stock`
--

CREATE TABLE `moduloapp_stock` (
  `id` bigint(20) NOT NULL,
  `nombre_producto` varchar(100) NOT NULL,
  `tipo_producto` varchar(100) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `id_producto_stock` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `moduloapp_sucursal`
--

CREATE TABLE `moduloapp_sucursal` (
  `id` bigint(20) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `numero_telefono` int(11) NOT NULL,
  `nombre` varchar(10) NOT NULL,
  `id_sucursal` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `moduloapp_categoria`
--
ALTER TABLE `moduloapp_categoria`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre_categoria` (`nombre_categoria`),
  ADD UNIQUE KEY `id_categoria` (`id_categoria`);

--
-- Indices de la tabla `moduloapp_devolucion`
--
ALTER TABLE `moduloapp_devolucion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `moduloApp_devolucion_nombre_producto_id_b115aa57` (`id_venta_id`);

--
-- Indices de la tabla `moduloapp_ingresarentradaproductos`
--
ALTER TABLE `moduloapp_ingresarentradaproductos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `moduloapp_ingresarsalidaproductos`
--
ALTER TABLE `moduloapp_ingresarsalidaproductos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `moduloapp_nombreproducto`
--
ALTER TABLE `moduloapp_nombreproducto`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `moduloApp_nombreproducto_id_producto_07ac0f51_uniq` (`id_producto`),
  ADD UNIQUE KEY `moduloApp_nombreproducto_nombreProducto_447280b2_uniq` (`nombre_producto`);

--
-- Indices de la tabla `moduloapp_producto`
--
ALTER TABLE `moduloapp_producto`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id_producto` (`id_producto`),
  ADD KEY `moduloApp_producto_sucursal_id_d9e5f4d7_fk_moduloApp_sucursal_id` (`sucursal_id`),
  ADD KEY `moduloApp_producto_tipo_producto_id_8065b36d` (`tipo_producto_id`),
  ADD KEY `moduloApp_producto_nombre_id_5af341ce` (`nombre_id`);

--
-- Indices de la tabla `moduloapp_rol`
--
ALTER TABLE `moduloapp_rol`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `moduloapp_stock`
--
ALTER TABLE `moduloapp_stock`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `moduloapp_sucursal`
--
ALTER TABLE `moduloapp_sucursal`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id_sucursal` (`id_sucursal`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=72;

--
-- AUTO_INCREMENT de la tabla `moduloapp_categoria`
--
ALTER TABLE `moduloapp_categoria`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `moduloapp_devolucion`
--
ALTER TABLE `moduloapp_devolucion`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `moduloapp_ingresarentradaproductos`
--
ALTER TABLE `moduloapp_ingresarentradaproductos`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `moduloapp_ingresarsalidaproductos`
--
ALTER TABLE `moduloapp_ingresarsalidaproductos`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `moduloapp_nombreproducto`
--
ALTER TABLE `moduloapp_nombreproducto`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `moduloapp_producto`
--
ALTER TABLE `moduloapp_producto`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `moduloapp_rol`
--
ALTER TABLE `moduloapp_rol`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `moduloapp_stock`
--
ALTER TABLE `moduloapp_stock`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `moduloapp_sucursal`
--
ALTER TABLE `moduloapp_sucursal`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `moduloapp_devolucion`
--
ALTER TABLE `moduloapp_devolucion`
  ADD CONSTRAINT `moduloApp_devolucion_id_venta_id_64bd6581_fk_moduloApp` FOREIGN KEY (`id_venta_id`) REFERENCES `moduloapp_ingresarsalidaproductos` (`id`);

--
-- Filtros para la tabla `moduloapp_producto`
--
ALTER TABLE `moduloapp_producto`
  ADD CONSTRAINT `moduloApp_producto_nombre_id_5af341ce_fk_moduloApp` FOREIGN KEY (`nombre_id`) REFERENCES `moduloapp_nombreproducto` (`id`),
  ADD CONSTRAINT `moduloApp_producto_sucursal_id_d9e5f4d7_fk_moduloApp_sucursal_id` FOREIGN KEY (`sucursal_id`) REFERENCES `moduloapp_sucursal` (`id`),
  ADD CONSTRAINT `moduloApp_producto_tipo_producto_id_8065b36d_fk_moduloApp` FOREIGN KEY (`tipo_producto_id`) REFERENCES `moduloapp_categoria` (`id`);

--
-- Filtros para la tabla `moduloapp_rol`
--
ALTER TABLE `moduloapp_rol`
  ADD CONSTRAINT `moduloApp_rol_usuario_id_ce31350e_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
