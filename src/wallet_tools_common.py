import logging
from typing import Callable, Optional, Any, Tuple, List

import hw_intf
from app_config import AppConfig
from hw_common import HWDevice, HWType


log = logging.getLogger('dmt.wallet_tools_dlg')


class ActionPageBase:
    def __init__(self, parent_dialog, app_config: AppConfig, hw_devices: hw_intf.HWDevices, action_title: str):
        self.parent_dialog = parent_dialog
        self.app_config = app_config
        self.hw_devices = hw_devices
        self.hw_devices.sig_connected_hw_device_changed.connect(self.on_connected_hw_device_changed)
        self.action_title = action_title
        self.fn_exit_page: Optional[Callable[[], None]] = None
        self.fn_set_action_title: Optional[Callable[[str], None]] = None
        self.fn_set_btn_cancel_visible: Optional[Callable[[bool], None]] = None
        self.fn_set_btn_cancel_enabled: Optional[Callable[[bool], None]] = None
        self.fn_set_btn_cancel_text: Optional[Callable[[str, str], None]] = None
        self.fn_set_btn_back_visible: Optional[Callable[[bool], None]] = None
        self.fn_set_btn_back_enabled: Optional[Callable[[bool], None]] = None
        self.fn_set_btn_back_text: Optional[Callable[[str, str], None]] = None
        self.fn_set_btn_continue_visible: Optional[Callable[[bool], None]] = None
        self.fn_set_btn_continue_enabled: Optional[Callable[[bool], None]] = None
        self.fn_set_btn_continue_text: Optional[Callable[[str, str], None]] = None
        self.fn_set_hw_change_enabled: Optional[Callable[[bool], None]] = None
        self.fn_show_message_page: Optional[Callable[[str], None]] = None
        self.fn_show_action_page: Optional[Callable[[None], None]] = None

    def set_control_functions(
            self,
            fn_exit_page: Callable[[], None],
            fn_set_action_title: Callable[[str], None],
            fn_set_btn_cancel_visible: Callable[[bool], None],
            fn_set_btn_cancel_enabled: Callable[[bool], None],
            fn_set_btn_cancel_text: Callable[[str, str], None],
            fn_set_btn_back_visible: Callable[[bool], None],
            fn_set_btn_back_enabled: Callable[[bool], None],
            fn_set_btn_back_text: Callable[[str, str], None],
            fn_set_btn_continue_visible: Callable[[bool], None],
            fn_set_btn_continue_enabled: Callable[[bool], None],
            fn_set_btn_continue_text: Callable[[str, str], None],
            fn_set_hw_panel_visible: Callable[[bool], None],
            fn_set_hw_change_enabled: Callable[[bool], None],
            fn_show_message_page: Optional[Callable[[str], None]],
            fn_show_action_page: Optional[Callable[[None], None]]):

        self.fn_exit_page = fn_exit_page
        self.fn_set_action_title = fn_set_action_title
        self.fn_set_btn_cancel_visible = fn_set_btn_cancel_visible
        self.fn_set_btn_cancel_enabled = fn_set_btn_cancel_enabled
        self.fn_set_btn_cancel_text = fn_set_btn_cancel_text
        self.fn_set_btn_back_visible = fn_set_btn_back_visible
        self.fn_set_btn_back_enabled = fn_set_btn_back_enabled
        self.fn_set_btn_back_text = fn_set_btn_back_text
        self.fn_set_btn_continue_visible = fn_set_btn_continue_visible
        self.fn_set_btn_continue_enabled = fn_set_btn_continue_enabled
        self.fn_set_btn_continue_text = fn_set_btn_continue_text
        self.fn_set_hw_panel_visible = fn_set_hw_panel_visible
        self.fn_set_hw_change_enabled = fn_set_hw_change_enabled
        self.fn_show_message_page = fn_show_message_page
        self.fn_show_action_page = fn_show_action_page

    def initialize(self):
        self.update_action_subtitle('')

    def on_close(self):
        pass

    def on_connected_hw_device_changed(self, cur_hw_device: HWDevice):
        pass

    def exit_page(self):
        if self.fn_exit_page:
            self.fn_exit_page()

    def set_action_title(self, title: str):
        if self.fn_set_action_title:
            self.fn_set_action_title(title)

    def set_btn_cancel_visible(self, visible: bool):
        if self.fn_set_btn_cancel_visible:
            self.fn_set_btn_cancel_visible(visible)

    def set_btn_cancel_enabled(self, enabled: bool):
        if self.fn_set_btn_cancel_enabled:
            self.fn_set_btn_cancel_enabled(enabled)

    def set_btn_cancel_text(self, label: str, tool_tip: Optional[str] = None):
        if self.fn_set_btn_cancel_text:
            self.fn_set_btn_cancel_text(label, tool_tip)

    def set_btn_back_visible(self, visible: bool):
        if self.fn_set_btn_back_visible:
            self.fn_set_btn_back_visible(visible)

    def set_btn_back_enabled(self, enabled: bool):
        if self.fn_set_btn_back_enabled:
            self.fn_set_btn_back_enabled(enabled)

    def set_btn_back_text(self, label: str, tool_tip: Optional[str] = None):
        if self.fn_set_btn_back_text:
            self.fn_set_btn_back_text(label, tool_tip)

    def set_btn_continue_visible(self, visible: bool):
        if self.fn_set_btn_continue_visible:
            self.fn_set_btn_continue_visible(visible)

    def set_btn_continue_enabled(self, enabled: bool):
        if self.fn_set_btn_continue_enabled:
            self.fn_set_btn_continue_enabled(enabled)

    def set_btn_continue_text(self, label: str, tool_tip: Optional[str] = None):
        if self.fn_set_btn_continue_text:
            self.fn_set_btn_continue_text(label, tool_tip)

    def set_hw_panel_visible(self, visible: bool):
        if self.fn_set_hw_panel_visible:
            self.fn_set_hw_panel_visible(visible)

    def set_hw_change_enabled(self, enabled: bool):
        if self.fn_set_hw_change_enabled:
            self.fn_set_hw_change_enabled(enabled)

    def show_message_page(self, message: str):
        if self.fn_show_message_page:
            self.fn_show_message_page(message)

    def show_action_page(self):
        if self.fn_show_action_page:
            self.fn_show_action_page()

    def go_to_next_step(self):
        pass

    def go_to_prev_step(self):
        self.exit_page()

    def on_btn_continue_clicked(self):
        self.go_to_next_step()

    def on_btn_back_clicked(self):
        self.go_to_prev_step()

    def on_before_cancel(self) -> bool:
        """
        Called by the wallet tools dialog before closing dialog (after the <Close/Cancel> button has been clicked.
        :return: True if the action widget allows for closure or False otherwise.
        """
        return True

    def update_action_subtitle(self, subtitle: Optional[str] = None):
        title = 'Update hardware wallet firmware'
        if subtitle:
            title += ' - ' + subtitle
        self.set_action_title(f'<b>{title}</b>')


