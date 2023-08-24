--
-- PostgreSQL database dump
--

-- Dumped from database version 13.10 (Ubuntu 13.10-1.pgdg22.04+1)
-- Dumped by pg_dump version 13.10 (Ubuntu 13.10-1.pgdg22.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: calories; Type: TABLE; Schema: public; Owner: cahardy
--

CREATE TABLE public.calories (
    calorie_id integer NOT NULL,
    user_id integer,
    calories integer,
    date date,
    "time" time without time zone
);


ALTER TABLE public.calories OWNER TO cahardy;

--
-- Name: calories_calorie_id_seq; Type: SEQUENCE; Schema: public; Owner: cahardy
--

CREATE SEQUENCE public.calories_calorie_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.calories_calorie_id_seq OWNER TO cahardy;

--
-- Name: calories_calorie_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cahardy
--

ALTER SEQUENCE public.calories_calorie_id_seq OWNED BY public.calories.calorie_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: cahardy
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    email character varying(50),
    password character varying(30),
    fname character varying(30),
    lname character varying(30),
    birth date
);


ALTER TABLE public.users OWNER TO cahardy;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: cahardy
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO cahardy;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cahardy
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: weights; Type: TABLE; Schema: public; Owner: cahardy
--

CREATE TABLE public.weights (
    weight_id integer NOT NULL,
    user_id integer,
    date date,
    weight real
);


ALTER TABLE public.weights OWNER TO cahardy;

--
-- Name: weights_weight_id_seq; Type: SEQUENCE; Schema: public; Owner: cahardy
--

CREATE SEQUENCE public.weights_weight_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.weights_weight_id_seq OWNER TO cahardy;

--
-- Name: weights_weight_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cahardy
--

ALTER SEQUENCE public.weights_weight_id_seq OWNED BY public.weights.weight_id;


--
-- Name: calories calorie_id; Type: DEFAULT; Schema: public; Owner: cahardy
--

ALTER TABLE ONLY public.calories ALTER COLUMN calorie_id SET DEFAULT nextval('public.calories_calorie_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: cahardy
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Name: weights weight_id; Type: DEFAULT; Schema: public; Owner: cahardy
--

ALTER TABLE ONLY public.weights ALTER COLUMN weight_id SET DEFAULT nextval('public.weights_weight_id_seq'::regclass);


--
-- Data for Name: calories; Type: TABLE DATA; Schema: public; Owner: cahardy
--

COPY public.calories (calorie_id, user_id, calories, date, "time") FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: cahardy
--

COPY public.users (user_id, email, password, fname, lname, birth) FROM stdin;
\.


--
-- Data for Name: weights; Type: TABLE DATA; Schema: public; Owner: cahardy
--

COPY public.weights (weight_id, user_id, date, weight) FROM stdin;
\.


--
-- Name: calories_calorie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cahardy
--

SELECT pg_catalog.setval('public.calories_calorie_id_seq', 1, false);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cahardy
--

SELECT pg_catalog.setval('public.users_user_id_seq', 1, false);


--
-- Name: weights_weight_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cahardy
--

SELECT pg_catalog.setval('public.weights_weight_id_seq', 1, false);


--
-- Name: calories calories_pkey; Type: CONSTRAINT; Schema: public; Owner: cahardy
--

ALTER TABLE ONLY public.calories
    ADD CONSTRAINT calories_pkey PRIMARY KEY (calorie_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: cahardy
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: weights weights_pkey; Type: CONSTRAINT; Schema: public; Owner: cahardy
--

ALTER TABLE ONLY public.weights
    ADD CONSTRAINT weights_pkey PRIMARY KEY (weight_id);


--
-- Name: calories calories_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: cahardy
--

ALTER TABLE ONLY public.calories
    ADD CONSTRAINT calories_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: weights weights_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: cahardy
--

ALTER TABLE ONLY public.weights
    ADD CONSTRAINT weights_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- PostgreSQL database dump complete
--

