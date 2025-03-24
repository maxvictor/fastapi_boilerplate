from fastapi.responses import JSONResponse


def success_response(data, message="Success", status_code=200):
    return JSONResponse(
        status_code=status_code, content={"result": data, "message": message}
    )


def error_response(code: str, description: str, status_code=500):
    return JSONResponse(
        status_code=status_code, content={"code": code, "description": description}
    )
