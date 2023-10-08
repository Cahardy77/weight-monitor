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
    date timestamp without time zone,
    comment character varying(200)
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
    password character varying(20),
    fname character varying(20),
    lname character varying(20),
    birth timestamp without time zone,
    height integer,
    gender character varying(7),
    activity_level character varying(30),
    goal character varying(30)
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
-- Name: water; Type: TABLE; Schema: public; Owner: cahardy
--

CREATE TABLE public.water (
    water_id integer NOT NULL,
    user_id integer,
    water integer,
    date timestamp without time zone
);


ALTER TABLE public.water OWNER TO cahardy;

--
-- Name: water_water_id_seq; Type: SEQUENCE; Schema: public; Owner: cahardy
--

CREATE SEQUENCE public.water_water_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.water_water_id_seq OWNER TO cahardy;

--
-- Name: water_water_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cahardy
--

ALTER SEQUENCE public.water_water_id_seq OWNED BY public.water.water_id;


--
-- Name: weights; Type: TABLE; Schema: public; Owner: cahardy
--

CREATE TABLE public.weights (
    weight_id integer NOT NULL,
    user_id integer,
    weight double precision,
    date timestamp without time zone,
    comment character varying(200)
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
-- Name: water water_id; Type: DEFAULT; Schema: public; Owner: cahardy
--

ALTER TABLE ONLY public.water ALTER COLUMN water_id SET DEFAULT nextval('public.water_water_id_seq'::regclass);


--
-- Name: weights weight_id; Type: DEFAULT; Schema: public; Owner: cahardy
--

ALTER TABLE ONLY public.weights ALTER COLUMN weight_id SET DEFAULT nextval('public.weights_weight_id_seq'::regclass);


--
-- Data for Name: calories; Type: TABLE DATA; Schema: public; Owner: cahardy
--

COPY public.calories (calorie_id, user_id, calories, date, comment) FROM stdin;
1	1	30	2023-02-01 19:30:00	No comment
2	2	500	2023-04-01 13:15:00	No comment
3	3	600	2023-06-23 07:12:00	No comment
4	1	200	2023-05-01 19:30:00	No comment
5	1	100	2023-04-01 13:15:00	No comment
6	1	50	2023-06-23 07:12:00	No comment
7	1	800	2023-10-08 17:43:10	Chinese
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: cahardy
--

COPY public.users (user_id, email, password, fname, lname, birth, height, gender, activity_level, goal) FROM stdin;
1	chris@gmail.com	secret	Chris	Hardy	1996-05-01 00:00:00	72	male	moderately_active	weight_loss
2	john@gmail.com	secret	john	smith	1900-06-27 00:00:00	72	male	moderately_active	weight_loss
3	jane@gmail.com	secret	jane	doe	2000-01-15 00:00:00	72	male	moderately_active	weight_loss
\.


--
-- Data for Name: water; Type: TABLE DATA; Schema: public; Owner: cahardy
--

COPY public.water (water_id, user_id, water, date) FROM stdin;
1	1	10	2023-02-01 19:30:00
2	2	5	2023-04-01 13:15:00
3	3	7	2023-06-23 07:12:00
4	1	2	2023-09-18 19:30:00
5	1	5	2023-09-18 13:15:00
6	1	3	2023-09-18 07:12:00
7	1	15	2023-10-08 17:42:57
8	1	10	2023-10-08 17:45:06
\.


--
-- Data for Name: weights; Type: TABLE DATA; Schema: public; Owner: cahardy
--

COPY public.weights (weight_id, user_id, weight, date, comment) FROM stdin;
1	2	212.3	2023-02-01 16:00:00	No Comment.
2	3	195.6	2023-04-01 16:00:00	No Comment.
3	1	240	2023-08-01 16:00:00	No Comment.
4	1	239	2023-08-02 16:00:00	No Comment.
5	1	240	2023-08-03 16:00:00	No Comment.
6	1	238	2023-08-04 16:00:00	No Comment.
7	1	236	2023-08-05 16:00:00	No Comment.
8	1	234	2023-08-06 16:00:00	No Comment.
9	1	237	2023-08-07 16:00:00	No Comment.
10	1	234	2023-08-08 16:00:00	No Comment.
11	1	230	2023-08-09 16:00:00	No Comment.
12	1	229	2023-08-10 16:00:00	No Comment.
13	1	225	2023-08-11 16:00:00	No Comment.
14	1	226	2023-08-12 16:00:00	No Comment.
15	1	227	2023-08-13 16:00:00	No Comment.
16	1	224	2023-08-14 16:00:00	No Comment.
17	1	223	2023-08-15 16:00:00	No Comment.
18	1	220	2023-08-16 16:00:00	No Comment.
19	1	221	2023-08-17 16:00:00	No Comment.
20	1	226	2023-08-18 16:00:00	No Comment.
21	1	234	2023-08-19 16:00:00	No Comment.
22	1	230	2023-08-20 16:00:00	No Comment.
23	1	228	2023-08-21 16:00:00	No Comment.
24	1	226	2023-08-22 16:00:00	No Comment.
25	1	220	2023-08-23 16:00:00	No Comment.
26	1	218	2023-08-24 16:00:00	No Comment.
27	1	210	2023-08-25 16:00:00	No Comment.
28	1	212	2023-08-26 16:00:00	No Comment.
29	1	210	2023-08-27 16:00:00	No Comment.
30	1	206	2023-08-28 16:00:00	No Comment.
31	1	204	2023-08-29 16:00:00	No Comment.
32	1	206	2023-08-30 16:00:00	No Comment.
33	1	200	2023-08-31 16:00:00	No Comment.
34	1	210	2023-09-14 16:00:00	Exercised arms today.
35	1	209.5	2023-09-15 16:00:00	Leg day.
36	1	209.6	2023-09-16 16:00:00	Worked and then worked on project.
37	1	209.4	2023-09-17 16:00:00	Worked and relaxed after work.
38	1	209.3	2023-09-18 16:00:00	Worked on core today.
39	1	208	2023-10-08 17:43:27	Worked on cars
\.


--
-- Name: calories_calorie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cahardy
--

SELECT pg_catalog.setval('public.calories_calorie_id_seq', 7, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cahardy
--

SELECT pg_catalog.setval('public.users_user_id_seq', 3, true);


--
-- Name: water_water_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cahardy
--

SELECT pg_catalog.setval('public.water_water_id_seq', 8, true);


--
-- Name: weights_weight_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cahardy
--

SELECT pg_catalog.setval('public.weights_weight_id_seq', 39, true);


--
-- Name: calories calories_pkey; Type: CONSTRAINT; Schema: public; Owner: cahardy
--

ALTER TABLE ONLY public.calories
    ADD CONSTRAINT calories_pkey PRIMARY KEY (calorie_id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: cahardy
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: cahardy
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: water water_pkey; Type: CONSTRAINT; Schema: public; Owner: cahardy
--

ALTER TABLE ONLY public.water
    ADD CONSTRAINT water_pkey PRIMARY KEY (water_id);


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
-- Name: water water_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: cahardy
--

ALTER TABLE ONLY public.water
    ADD CONSTRAINT water_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: weights weights_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: cahardy
--

ALTER TABLE ONLY public.weights
    ADD CONSTRAINT weights_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- PostgreSQL database dump complete
--

