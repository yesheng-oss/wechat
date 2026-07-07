import importlib.util
import pathlib
import unittest


def load_send_many_msg():
    module_path = pathlib.Path(__file__).resolve().parents[1] / "wxauto" / "batch.py"
    spec = importlib.util.spec_from_file_location("wxauto_batch", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.send_many_msg


class FakeWeChat:
    def __init__(self, fail_on=None):
        self.fail_on = set(fail_on or [])
        self.calls = []

    def SendMsg(self, msg, who=None, clear=True, at=None):
        self.calls.append(
            {
                "msg": msg,
                "who": who,
                "clear": clear,
                "at": at,
            }
        )
        if who in self.fail_on:
            raise RuntimeError(f"failed to send to {who}")


class SendManyMsgTests(unittest.TestCase):
    def test_send_many_msg_returns_success_and_failure_results(self):
        fake = FakeWeChat(fail_on={"李四"})
        send_many_msg = load_send_many_msg()

        result = send_many_msg(
            fake.SendMsg,
            "周报已更新",
            ["张三", "李四", "王五"],
            clear=False,
            at=["产品经理"],
        )

        self.assertEqual(
            fake.calls,
            [
                {"msg": "周报已更新", "who": "张三", "clear": False, "at": ["产品经理"]},
                {"msg": "周报已更新", "who": "李四", "clear": False, "at": ["产品经理"]},
                {"msg": "周报已更新", "who": "王五", "clear": False, "at": ["产品经理"]},
            ],
        )
        self.assertEqual(result["success"], ["张三", "王五"])
        self.assertEqual(list(result["failed"]), ["李四"])
        self.assertIn("failed to send to 李四", result["failed"]["李四"])

    def test_send_many_msg_rejects_string_recipients(self):
        fake = FakeWeChat()
        send_many_msg = load_send_many_msg()

        with self.assertRaises(TypeError):
            send_many_msg(fake.SendMsg, "hello", "张三")


if __name__ == "__main__":
    unittest.main()
