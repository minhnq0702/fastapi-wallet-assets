#  -*- encoding: utf-8 -*-
import pytest

from app.core.security import encrypt, verify_password

PASSWORD = "test-password"


class TestSecurity:
    """Security test\n
    Test hash/verify password
    """
    @pytest.fixture
    def test_hash_password(self):
        """Test hash password successfully
        """
        hashed_password = encrypt(PASSWORD)
        assert hashed_password != PASSWORD
        return hashed_password

    def test_correct_password(self, test_hash_password):
        """Test hash password and verify successfully
        """
        verify = verify_password(PASSWORD, test_hash_password)
        assert verify is True

    def test_wrong_password(self, test_hash_password):
        """Test hash password and verify fail
        """
        verify = verify_password("another-password", test_hash_password)
        assert verify is False
