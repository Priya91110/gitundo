def test_upload_api(request):
    sub_id = 866634343
    request_id = 1111
    test = upload_api(sub_id, request_id)
    assert test=="111", "Error found 404"
    