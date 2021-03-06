PGDMP     $    $                 x         	   DashLearn    12.1    12.1 f    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16512 	   DashLearn    DATABASE     �   CREATE DATABASE "DashLearn" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_Malaysia.1252' LC_CTYPE = 'English_Malaysia.1252';
    DROP DATABASE "DashLearn";
                postgres    false            �            1259    16526    accounts_account    TABLE     �  CREATE TABLE public.accounts_account (
    id integer NOT NULL,
    password character varying(140) NOT NULL,
    program character varying(120) NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_admin boolean NOT NULL,
    is_active boolean NOT NULL,
    is_staff boolean NOT NULL,
    is_superuser boolean NOT NULL,
    matric character varying(10) NOT NULL,
    cgpa real,
    name character varying,
    cgpapercent integer
);
 $   DROP TABLE public.accounts_account;
       public         heap    postgres    false            �            1259    16524    accounts_account_id_seq    SEQUENCE     �   CREATE SEQUENCE public.accounts_account_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.accounts_account_id_seq;
       public          postgres    false    205            �           0    0    accounts_account_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.accounts_account_id_seq OWNED BY public.accounts_account.id;
          public          postgres    false    204            �            1259    24615 
   assignment    TABLE       CREATE TABLE public.assignment (
    id bigint NOT NULL,
    "courseId" character varying,
    matric character varying,
    feedback character varying DEFAULT 'No Feedback Yet'::character varying,
    "dueDate" date,
    status boolean DEFAULT false,
    name character varying
);
    DROP TABLE public.assignment;
       public         heap    postgres    false            �            1259    24613    assignment_id_seq    SEQUENCE     z   CREATE SEQUENCE public.assignment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.assignment_id_seq;
       public          postgres    false    224            �           0    0    assignment_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.assignment_id_seq OWNED BY public.assignment.id;
          public          postgres    false    223            �            1259    16583 
   auth_group    TABLE     f   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
    DROP TABLE public.auth_group;
       public         heap    postgres    false            �            1259    16581    auth_group_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public          postgres    false    213            �           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
          public          postgres    false    212            �            1259    16593    auth_group_permissions    TABLE     �   CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         heap    postgres    false            �            1259    16591    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public          postgres    false    215            �           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
          public          postgres    false    214            �            1259    16575    auth_permission    TABLE     �   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         heap    postgres    false            �            1259    16573    auth_permission_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public          postgres    false    211            �           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
          public          postgres    false    210            �            1259    24578    course    TABLE     �   CREATE TABLE public.course (
    "courseId" bigint NOT NULL,
    "courseCode" character varying,
    semester integer,
    year character varying,
    "group" integer
);
    DROP TABLE public.course;
       public         heap    postgres    false            �            1259    24590    coursePerformance    TABLE     �  CREATE TABLE public."coursePerformance" (
    id bigint NOT NULL,
    courseid integer,
    matric character varying,
    attendance real,
    "cps4W7" real DEFAULT 0.0,
    "cps7W7" real DEFAULT 0.0,
    "cps4W14" real DEFAULT 0.0,
    "cps7W14" real DEFAULT 0.0,
    amali real DEFAULT 0.0,
    quiz real DEFAULT 0.0,
    "cps4Final" real DEFAULT 0.0,
    "cps7Final" real DEFAULT 0.0,
    "cps8Final" real DEFAULT 0.0,
    total real DEFAULT 0.0,
    status boolean DEFAULT true,
    "couseCode" character varying,
    week7 real DEFAULT 0.0,
    week14 real DEFAULT 0.0,
    "totalT1T2" real,
    "totalCarryMark" real,
    "predictedMarks" real
);
 '   DROP TABLE public."coursePerformance";
       public         heap    postgres    false            �            1259    24588    coursePerformance_id_seq    SEQUENCE     �   CREATE SEQUENCE public."coursePerformance_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public."coursePerformance_id_seq";
       public          postgres    false    222            �           0    0    coursePerformance_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public."coursePerformance_id_seq" OWNED BY public."coursePerformance".id;
          public          postgres    false    221            �            1259    24576    course_courseId_seq    SEQUENCE     ~   CREATE SEQUENCE public."course_courseId_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public."course_courseId_seq";
       public          postgres    false    220            �           0    0    course_courseId_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public."course_courseId_seq" OWNED BY public.course."courseId";
          public          postgres    false    219            �            1259    16551    django_admin_log    TABLE     �  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         heap    postgres    false            �            1259    16549    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public          postgres    false    209            �           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
          public          postgres    false    208            �            1259    16541    django_content_type    TABLE     �   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         heap    postgres    false            �            1259    16539    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public          postgres    false    207            �           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
          public          postgres    false    206            �            1259    16515    django_migrations    TABLE     �   CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         heap    postgres    false            �            1259    16513    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public          postgres    false    203            �           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
          public          postgres    false    202            �            1259    16625    django_session    TABLE     �   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         heap    postgres    false            �            1259    16635    marks    TABLE     �   CREATE TABLE public.marks (
    matric character varying NOT NULL,
    su1 integer,
    smid integer,
    sfin integer,
    att real,
    mu1 integer,
    mmid integer,
    mfin integer
);
    DROP TABLE public.marks;
       public         heap    postgres    false            �            1259    16651    program    TABLE     �   CREATE TABLE public.program (
    "programId" character varying NOT NULL,
    "programName" character varying,
    intake integer,
    "Faculty" character varying
);
    DROP TABLE public.program;
       public         heap    postgres    false            �
           2604    16529    accounts_account id    DEFAULT     z   ALTER TABLE ONLY public.accounts_account ALTER COLUMN id SET DEFAULT nextval('public.accounts_account_id_seq'::regclass);
 B   ALTER TABLE public.accounts_account ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    205    204    205            �
           2604    24618    assignment id    DEFAULT     n   ALTER TABLE ONLY public.assignment ALTER COLUMN id SET DEFAULT nextval('public.assignment_id_seq'::regclass);
 <   ALTER TABLE public.assignment ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    223    224    224            �
           2604    16586    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    213    212    213            �
           2604    16596    auth_group_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    214    215            �
           2604    16578    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    210    211    211            �
           2604    24581    course courseId    DEFAULT     v   ALTER TABLE ONLY public.course ALTER COLUMN "courseId" SET DEFAULT nextval('public."course_courseId_seq"'::regclass);
 @   ALTER TABLE public.course ALTER COLUMN "courseId" DROP DEFAULT;
       public          postgres    false    219    220    220            �
           2604    24593    coursePerformance id    DEFAULT     �   ALTER TABLE ONLY public."coursePerformance" ALTER COLUMN id SET DEFAULT nextval('public."coursePerformance_id_seq"'::regclass);
 E   ALTER TABLE public."coursePerformance" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    222    221    222            �
           2604    16554    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    209    208    209            �
           2604    16544    django_content_type id    DEFAULT     �   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    207    206    207            �
           2604    16518    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    203    202    203            �          0    16526    accounts_account 
   TABLE DATA           �   COPY public.accounts_account (id, password, program, date_joined, last_login, is_admin, is_active, is_staff, is_superuser, matric, cgpa, name, cgpapercent) FROM stdin;
    public          postgres    false    205   1�       �          0    24615 
   assignment 
   TABLE DATA           _   COPY public.assignment (id, "courseId", matric, feedback, "dueDate", status, name) FROM stdin;
    public          postgres    false    224    �       �          0    16583 
   auth_group 
   TABLE DATA           .   COPY public.auth_group (id, name) FROM stdin;
    public          postgres    false    213   ��       �          0    16593    auth_group_permissions 
   TABLE DATA           M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public          postgres    false    215   ��       �          0    16575    auth_permission 
   TABLE DATA           N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public          postgres    false    211   ȇ       �          0    24578    course 
   TABLE DATA           S   COPY public.course ("courseId", "courseCode", semester, year, "group") FROM stdin;
    public          postgres    false    220   ݉       �          0    24590    coursePerformance 
   TABLE DATA           	  COPY public."coursePerformance" (id, courseid, matric, attendance, "cps4W7", "cps7W7", "cps4W14", "cps7W14", amali, quiz, "cps4Final", "cps7Final", "cps8Final", total, status, "couseCode", week7, week14, "totalT1T2", "totalCarryMark", "predictedMarks") FROM stdin;
    public          postgres    false    222   �       �          0    16551    django_admin_log 
   TABLE DATA           �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public          postgres    false    209   �       �          0    16541    django_content_type 
   TABLE DATA           C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public          postgres    false    207   �       �          0    16515    django_migrations 
   TABLE DATA           C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public          postgres    false    203   ��       �          0    16625    django_session 
   TABLE DATA           P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public          postgres    false    216   ��       �          0    16635    marks 
   TABLE DATA           N   COPY public.marks (matric, su1, smid, sfin, att, mu1, mmid, mfin) FROM stdin;
    public          postgres    false    217   ?�       �          0    16651    program 
   TABLE DATA           P   COPY public.program ("programId", "programName", intake, "Faculty") FROM stdin;
    public          postgres    false    218   "�       �           0    0    accounts_account_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.accounts_account_id_seq', 187, true);
          public          postgres    false    204            �           0    0    assignment_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.assignment_id_seq', 78, true);
          public          postgres    false    223            �           0    0    auth_group_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);
          public          postgres    false    212            �           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
          public          postgres    false    214            �           0    0    auth_permission_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_permission_id_seq', 52, true);
          public          postgres    false    210            �           0    0    coursePerformance_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public."coursePerformance_id_seq"', 524, true);
          public          postgres    false    221            �           0    0    course_courseId_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public."course_courseId_seq"', 3, true);
          public          postgres    false    219            �           0    0    django_admin_log_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);
          public          postgres    false    208            �           0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 13, true);
          public          postgres    false    206            �           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 20, true);
          public          postgres    false    202            �
           2606    16537 ,   accounts_account accounts_account_matric_key 
   CONSTRAINT     i   ALTER TABLE ONLY public.accounts_account
    ADD CONSTRAINT accounts_account_matric_key UNIQUE (matric);
 V   ALTER TABLE ONLY public.accounts_account DROP CONSTRAINT accounts_account_matric_key;
       public            postgres    false    205            �
           2606    16531 &   accounts_account accounts_account_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.accounts_account
    ADD CONSTRAINT accounts_account_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.accounts_account DROP CONSTRAINT accounts_account_pkey;
       public            postgres    false    205                       2606    24623    assignment assignment_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.assignment
    ADD CONSTRAINT assignment_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.assignment DROP CONSTRAINT assignment_pkey;
       public            postgres    false    224            �
           2606    16623    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public            postgres    false    213            �
           2606    16619 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public            postgres    false    215    215                       2606    16598 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public            postgres    false    215            �
           2606    16588    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public            postgres    false    213            �
           2606    16605 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public            postgres    false    211    211            �
           2606    16580 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public            postgres    false    211                       2606    24598 (   coursePerformance coursePerformance_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public."coursePerformance"
    ADD CONSTRAINT "coursePerformance_pkey" PRIMARY KEY (id);
 V   ALTER TABLE ONLY public."coursePerformance" DROP CONSTRAINT "coursePerformance_pkey";
       public            postgres    false    222                       2606    24586    course course_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.course
    ADD CONSTRAINT course_pkey PRIMARY KEY ("courseId");
 <   ALTER TABLE ONLY public.course DROP CONSTRAINT course_pkey;
       public            postgres    false    220            �
           2606    16560 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public            postgres    false    209            �
           2606    16548 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public            postgres    false    207    207            �
           2606    16546 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public            postgres    false    207            �
           2606    16523 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public            postgres    false    203                       2606    16632 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public            postgres    false    216                       2606    16642    marks marks_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.marks
    ADD CONSTRAINT marks_pkey PRIMARY KEY (matric);
 :   ALTER TABLE ONLY public.marks DROP CONSTRAINT marks_pkey;
       public            postgres    false    217            
           2606    16658    program program_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.program
    ADD CONSTRAINT program_pkey PRIMARY KEY ("programId");
 >   ALTER TABLE ONLY public.program DROP CONSTRAINT program_pkey;
       public            postgres    false    218            �
           1259    16538 %   accounts_account_matric_47201912_like    INDEX     x   CREATE INDEX accounts_account_matric_47201912_like ON public.accounts_account USING btree (matric varchar_pattern_ops);
 9   DROP INDEX public.accounts_account_matric_47201912_like;
       public            postgres    false    205            �
           1259    16624    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public            postgres    false    213            �
           1259    16620 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public            postgres    false    215                        1259    16621 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public            postgres    false    215            �
           1259    16606 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public            postgres    false    211            �
           1259    16571 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public            postgres    false    209            �
           1259    16572 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public            postgres    false    209                       1259    16634 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public            postgres    false    216                       1259    16633 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public            postgres    false    216                       2606    16613 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public          postgres    false    215    2807    211                       2606    16608 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public          postgres    false    213    215    2812                       2606    16599 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public          postgres    false    207    211    2798                       2606    16561 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public          postgres    false    2798    207    209                       2606    16566 I   django_admin_log django_admin_log_user_id_c564eba6_fk_accounts_account_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_accounts_account_id FOREIGN KEY (user_id) REFERENCES public.accounts_account(id) DEFERRABLE INITIALLY DEFERRED;
 s   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_accounts_account_id;
       public          postgres    false    209    205    2794            �   �  x�͘�n�P�ד�`�]���w�Fb�R���jSh+$t�8�;?��6y5<��\*bǍ����trfΙHca}�����m�Tb������ps�ތg�w��Y�{t�Q�n��^�7��gW7��&��Z�$��D�JHۗ�/��A����
��O����J�T�B�PiA��j��@������\Y�)ؤ#�o_��`NZf19j��\n��Y�JU�ϫ�}1�?����g��l����m����.Gs<9Y��ߞ�ƌ�0sb�<�\Q;�����8^�Z2�A8vU�`UG0��WY8(w@�Ye��Il~H�&sU�n��U���dVk0fq���UU�x1�8\Z2L+,\6e�V�ĸI��h��`\�ܢa\?h&X\R�q��|�2,�'ˉp��8ь7.�K�&����Oّl:Ͳ��޷�<4�l@�������e^ �0�|0	��"�7�ݝ��4�`� ��aY�/�v�a�	�*i��6WF6065��8�����1v���c��ۗy{C`������Q��@~Ȃ����WF	o��>�`Ӂa}	c5���nm@�f	���8�� o
6H[_�c�IS�ƹ�R��@ı�#���ծH�2N�&�o�Lk	F��2)��k�?z��K��sw�jK{<pi���,\������!�,��譫���>^g��|�?���?<5��@� x���{?���l�;��N���O�      �   ^  x����N�@��s�)�j�cvf��N&^��h��j||!p�%4�ܙ_���6��]�.4>��욇��Jy}Y���S��|n}h=7o�|�h�NfΌ�:ߺx	�q�_���̬�}����UVݶXY�ir�0E$�E����	�A>�f�X�!@H� RE0*�5�� Ip�.x��� ͡Vur�(�¸�'dZg��%B��I��L���2-
Iq"(�"@!�"�5C�U2-�^A�������kBq�I��]�����Ad��;�zBֹa(YgF�H��"��W(�H�_�؏������.۱�76����2�pD���b���4���X�������g\�      �      x������ � �      �      x������ � �      �     x�e��n�0F����LM��\�5&M�X��M}��c�vzG��@?�μ�a.��m�vqX��qf]�kXZH��.**�� ��[\4�J� �^�¶CM6�ǩ���u�5.؃�S �	�(����=��"�Qp�l�M��n*�g��R���'�AD<� �]e�v�����=�D��U���N����V���4�*���瘾m¸��$e�Aό��#c�G�߳C`���.a	� :ۣ��pE��� *$@$����I���3�#\�֫��>^���5!x=""�� n�e�}�S�6�5Ul�/�M��o�����-ǸWM'`�:F9��m�ǰ�3���V*�̠e�T�C���h3V�D�5Q�ЯY7� �\��
�FIN�*ߚ&G�ks�&UA:15��s80�������1��JO��pHT-�18�6��w^��ԇW���Ug����Y���|��x5uNt�4vS�K���n/�����}�5q���J݄�Ǜ����l      �   /   x�3��6640�BK}#N.#��\̈�*f3����� ~�      �   �  x���Mn�0�ך��D���ɶ����GR�I�Z.<�x��||$��z#�j�9��fM�6k�~~>���׏Ag�o$mP��b���w .�� � j� �@�w3�����h&��J�8 t�Ռo��oi�޺7F����P*�"��b� �l��yD�+��,�V
���6�����`ⴝ��dd�mD}U�BD������r<? �75 F!72	�Kwb"X��T���๢������3�M�)2Y�4G�~���Ҳy��%c�q�%H���$��PV5 e/a�Sv٫H{sD]+!�&3b��F��Z
���w�פ2��µzT������+T��`�C��+�>ɚ�DP��e�2+<��l7�#�&�Ke35F�Q��.�l;.A;H�J�(p�U`}t��KИ0�RVSG^W���M�.,��,�󻺙ʣ�1ۄ%�8�E��F��z$��ʮv��+���i�iy��(��p�V��bW`��6��j�����+��z���rkL�7c�yv/�́��%��˭.�g��#D���kE�ZQQ���.Q���G�E@���)F\��h�A��e�	I���/5�z��$��_��=�c�I.�{kPF����.D�v9�Y��E�IU$�ѵ���1(�l����o@x"��t�YB����
���� �RCW�ؽ#3��!�Q!r��Q禹��%(2����8��^b���]"��`�c7�e��Z,S��rƐ[-�h� �9V�>�$T���Y�i���k0Z;�j��y��������^ǋ Ѣl���'������8`����2ѧ]RJ���|Y{��!����0߉�h���wl�O��G��X�rx��3���Z�Q��b /[Zd��-i���,�u�� ʕ����_���
e�qJ������xyD��=6��;k��ׯ��z���A�      �      x������ � �      �   �   x�]�K�0D��ai�ޅ���PA��N�=�D�<�4�q@S�)�d]q *�k���$8~H�T܁O�k4�[op���	< y��d��2��Hz7<5P�I#�g<7����A"��k�5F7���ڍݤ���A�'�s\W      �   �  x����n� ���St�h�y�+!�P�6.�U���8��(� �p��93��i?q�  �\t����#�Q�zyu ʹ���ܑ_*����D��P�� .���U�h�ϣ}%��1+YeN�^�H����$Dw�Ma�Y��/{IݜN�&�Ȍ�Ơ7F�i�D��ޙV7�5��m�d��ğ��5�eC�=��n�P�\f��R���@�(UY�VEj[mУ���\D��{�;;���&JH�������޸�)F	����1y)	�1>�T
�ia������bn�K���o2F
���:u�svamI�ζ=�P�.�"�T�L�N&�0���!��{;M�}4,J��/�'7�y�s�'���z�?�F������T�<��A"�ũuz�<&����>ߍ�=$u^\�Q�d��Oo!*��<`�����䒤F�f;�� ߐ��>p5-��?�v�wRp�      �   �  x�Փ]o�8���_1��F��"�E[>
��H	���$�	6�i���~���4��߽u^�����{O_w�������p��[�齃��nxNl�lV�2�Y�����
Ӳhh^�e=��筢�}�^]��ǵUh�N��2����xJ�l]�M��*�5Jj�>ڭ�e�f�#�c����	�c�B��[�E�<*.�
��/tF��<�N,�m�| <"W��Qlv8X�\Y</Z� �P$ZJ���������y����hi���@�@�o�& p�=�}���v�Нb<s����ۼn�}�����nU�Gy��}�]����ІD�����\
�c��M�FL�`�Q�S��4����|��J_�\��B��jyb%~ێXn;Պ�
a���g����rxb%=�7����r��Z�v�zG���XQ+Z!�/�C�J�0�(R7�j�-���K��/X��%�:��Ct�/ ϱ5��v����`��wqc{��v���t�=���������_i^K����i�B��HC�ǀ�2�B*6�+�?ggS�b��v�M;���l�x`tc��ZY׮�w-�	��&O��Nx�¾�	A�<�D�-�b�jf3}�\e=���6�Q�m��i�1�?gG�������;�����6c�¸ӓ�}4@�ܞM�\wvc������;^���      �   �  x�U�٭�0C��b.�/ML��:����Ĳ$���r�9�NMg��9}���ni�(�;�Z:S�Ҟ��;
�m-�����iq��3d����(ds���d{(������g:U��=k*>�ˊ�oA�:�u|�u1���h
kl����Kסu⤕�2���d�E����l���eLDiQ���S��N�Q�2� ���l��/Z����Qz��ƻ��p���x�0��4HE��䈔b~8��A%k�U1��V����\����Y�L��%*��q���ꄩG�ˬZo4�9nU���N*���Q9�ez�]<�Օk�>-�Yu(�xɔd9j��H�m��$p����합�u���~:�ꊦ�U����Q�T����	��1ngUB?\E��P~�)D��M�j�2U�0!�Es����Q�h��o��%骛�6����� ���Z��ԩz��Dr=Ѷx���+Bَ�Mk�i:zt��_���&� 2�8@˝T4hxT�L�Z#ZS�+L�
ڒ�U���QJQ�ѿ)�����Kb> c}�A6�E�Ì�V��-����hC�+؎ڨh�;G�YW�	#�t�k�0^�R�����jxfI�d��EV륽hݹ*.R��;Lhw(�p"7b�� �-���b3�yʭ#(��0{�вS1�31-W�NH#Sԍ��I����,"=5.ߢ��������TH|���-4WL�1�H��ǁ���nQ4�����f���M��I3)�}�aP'��0�#ۦM:�R�Y����\�¼sd�K�P3%R���L��vjp���������@x�zײ�}"bY	�k:W~Y��V����{G�o�֢�O���R���Zd2
 [ւ��t�:,^�ɴ����lQ�q��4�H[;�8�h�{>�
~=ԧ�XO�����yW+ﰂ�)4��>X=�+���V��Z�sSW��3�xj{�
�g���e��*ѧ�L�jP�i������okb�      �   5   x�3��O+)O,JUp�K��KM-��K�4204�t���2©��"F��� Z��     