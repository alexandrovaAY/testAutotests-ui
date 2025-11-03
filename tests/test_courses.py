import pytest
from playwright.sync_api import expect, Page

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
        courses_text = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
        expect(courses_text).to_be_visible()
        expect(courses_text).to_have_text("Courses")

        courses_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
        expect(courses_icon).to_be_visible()

        title_text = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
        expect(title_text).to_be_visible()
        expect(title_text).to_have_text("There is no results")

        description_text = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
        expect(description_text).to_be_visible()
        expect(description_text).to_have_text("Results from the load test pipeline will be displayed here")
