CREATE TABLE IF NOT EXISTS public."user" (
    "id" text NOT NULL,
    "name" text NOT NULL,
    "email" text NOT NULL,
    "emailVerified" boolean DEFAULT false NOT NULL,
    "image" text,
    "createdAt" timestamp without time zone DEFAULT now() NOT NULL,
    "updatedAt" timestamp without time zone DEFAULT now() NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (email)
);

CREATE TABLE IF NOT EXISTS public."account" (
    "id" text NOT NULL,
    "accountId" text NOT NULL,
    "providerId" text NOT NULL,
    "userId" text NOT NULL,
    "accessToken" text,
    "refreshToken" text,
    "idToken" text,
    "accessTokenExpiresAt" timestamp without time zone,
    "refreshTokenExpiresAt" timestamp without time zone,
    "scope" text,
    "password" text,
    "createdAt" timestamp without time zone DEFAULT now() NOT NULL,
    "updatedAt" timestamp without time zone DEFAULT now() NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY ("userId") REFERENCES public."user"(id)
        ON DELETE CASCADE 
        ON UPDATE CASCADE,
    CONSTRAINT uq_provider_account UNIQUE ("providerId", "accountId")
);

CREATE TABLE IF NOT EXISTS public."session" (
    "id" text NOT NULL,
    "expiresAt" timestamp without time zone NOT NULL,
    "token" text NOT NULL,
    "createdAt" timestamp without time zone DEFAULT now() NOT NULL,
    "updatedAt" timestamp without time zone DEFAULT now() NOT NULL,
    "ipAddress" text,
    "userAgent" text,
    "userId" text NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (token),
    FOREIGN KEY ("userId") REFERENCES public."user"(id) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS public."verification" (
    "id" text NOT NULL,
    "identifier" text NOT NULL,
    "value" text NOT NULL,
    "expiresAt" timestamp without time zone NOT NULL,
    "createdAt" timestamp without time zone DEFAULT now() NOT NULL,
    "updatedAt" timestamp without time zone DEFAULT now() NOT NULL,
    PRIMARY KEY (id)
);

CREATE INDEX IF NOT EXISTS idx_session_token_expires ON public."session"("token", "expiresAt");
CREATE INDEX IF NOT EXISTS idx_session_userid ON public."session"("userId");