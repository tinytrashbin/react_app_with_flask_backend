#!/usr/bin/env python3

import unittest
import sys
import backend
import time

g_session = {}

tables = ["users" ]
ADMIN = "ADMIN"
ERROR_KEY = "error"

flags = ["--clean_database_at_start", '--dont_clean_database_at_end']
# flags = []

db = backend.db

class TestStringMethods(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    if "--clean_database_at_start" in flags:
      cls.cleanDatabase()
    for table in tables:
      query = f"SELECT count(*) as num from {table}" + (" WHERE role != 'ADMIN'" if table == "users" else "")
      assert db.readQuery(query)[0]["num"] == 0, f"Table {table} should not have data when running these unittests. Drop all tables and recreate them again to reach at clean stage."

  @classmethod
  def cleanDatabase(cls):
    for table in tables:
      query = f"DELETE from {table}" + (" WHERE role != 'ADMIN'" if table == "users" else "")
      db.writeQuery(query)

  @classmethod
  def tearDownClass(cls):
    if '--dont_clean_database_at_end' not in flags:
      cls.cleanDatabase()

  def step_login_signup(self):
    signup_ids = []
    for (name, email, password) in [("Name1", "n1@g.com", "p1"),
                                    ("Name2", "n2@g.com", "p2"),
                                    ("Name3", "n3@g.com", "p3")]:
      response = backend.SignUp(dict(name=name, email=email, password=password), g_session)
      self.assertNotEqual(g_session, {})
      self.assertTrue("login_key" in g_session)
      self.assertTrue("id" in g_session["login_key"])
      self.assertEqual(g_session["login_key"].get("role"), backend.DEFAULT_ROLE)
      self.assertEqual(g_session["login_key"].get("id"), response["id"])
      signup_id = response["id"]
      signup_ids.append(signup_id)
      self.assertEqual(g_session["login_key"].get("name"), name)
      self.assertTrue(response["id"] > 0)
      backend.Logout({}, g_session)
      self.assertTrue("login_key" not in g_session or "id" not in g_session["login_key"])

      response = backend.Login(dict(email=email, password=password), g_session)
      self.assertTrue("login_key" in g_session)
      self.assertTrue("id" in g_session["login_key"])
      self.assertEqual(g_session["login_key"].get("role"), backend.DEFAULT_ROLE)
      self.assertEqual(g_session["login_key"].get("id"), response["id"])
      self.assertEqual(g_session["login_key"].get("id"), signup_id)
      self.assertEqual(g_session["login_key"].get("name"), name)
      backend.Logout({}, g_session)
      self.assertTrue("login_key" not in g_session or "id" not in g_session["login_key"])

    self.student_id1 = signup_ids[0]
    self.student_id2 = signup_ids[1]
    self.student_id3 = signup_ids[2]
    response = backend.Login(dict(email="name3@g.com", password="p2"), g_session)
    self.assertTrue(ERROR_KEY in response)
    response = backend.Login(dict(email="name2@g.com", password="p3"), g_session)
    self.assertTrue(ERROR_KEY in response)

  def login(self, email, password):
    result = backend.Login(dict(email=email, password=password), g_session)
    self.assertTrue(ERROR_KEY not in result)
    return result


  def test_main(self):
    self.step_login_signup()


if __name__ == '__main__':
  unittest.main()
