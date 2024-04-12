from django.contrib.auth import models as auth_models
from django.contrib import auth
from django.contrib.auth.hashers import make_password


class FoodHubUserManager(auth_models.BaseUserManager):
    use_in_migrations = True

    def _create_user(self, first_name, last_name, email, username, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")

        if not username:
            raise ValueError("User must have an username")

        email = self.normalize_email(email)
        user = self.model(
            email = email,
            username = username,
            last_name = last_name,
            first_name = first_name,
            **extra_fields
        )
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, first_name, last_name, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(first_name, last_name, email, username, password, **extra_fields)

    def create_superuser(self, first_name, last_name, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(first_name, last_name, email, username, password, **extra_fields)

    def with_perm(
            self, perm, is_active=True, include_superusers=True, backend=None, obj=None
    ):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    "You have multiple authentication backends configured and "
                    "therefore must provide the `backend` argument."
                )
        elif not isinstance(backend, str):
            raise TypeError(
                "backend must be a dotted import path string (got %r)." % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, "with_perm"):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()