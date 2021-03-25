"""
Routes and views for the bottle application.
"""
from bottle import route, run, request, abort, post, delete, put, response, view, get, HTTPResponse
import jsonpickle
from coursemanager import manager
from datetime import datetime
from course import Course
from sqlalchemy import exc
from api_exceptions import NotFoundException


response.content_type = 'application/json'
props =  {'CRS_TITLE', 'FAC_CODE', 'INS_ID', 'DEP_CODE'}

@get('/')
def welcome():
    return HTTPResponse(status=200, body={"greetings" : "Hello there :) "})


@get('/courses')
def courses():
    """Get all courses"""
    try:
        return HTTPResponse(status=200, body=manager.getAll())
    except Exception as err:
        return HTTPResponse(status=500, body={"error" : err.args[0]})


@get('/courses/')
@get('/courses/:id')
def course(id=None):
    """Get a single course based on it's ID"""
    if id is None:
     return HTTPResponse(status=400, body={"error" : "You must specify an ID for the given route." })
    try:
        return HTTPResponse(status=200, body=manager.getOne(id))
    except NotFoundException as err:
        return HTTPResponse(status=404, body={"error" : str(err)})
    except Exception as err:
        return HTTPResponse(status=500, body={"error" : err.args[0]})




@post('/courses')
def create_course():
        """Create a single course based on a body parameter"""
        if(request.body):
            try:
                decoded_body = jsonpickle.decode(request.body.read())
                if all(k in decoded_body for k in props):
                 try:
                  return HTTPResponse(status=201, body=manager.createOne(decoded_body))              
                 except Exception as err:
                  return HTTPResponse(status=500, body={"error" : err.args[0]})

                else:
                 return HTTPResponse(status=422, body={"error" : "The given json property doesn't contain all the neccesary properties." })
            except:
                return HTTPResponse(status=400, body={"error" : "The given course data is not a valid json obj." })
            else:
                return HTTPResponse(status=400, body={"error" : "You must provide a request body to this method." })


@put('/courses/')
@put('/courses/:id')
def update_course(id=None):
    """Update a Course by it's ID """
    if id is None:
     return HTTPResponse(status=400, body={"error" : "You must specify an ID for the given route." })
    
     
    try:
                decoded_body = jsonpickle.decode(request.body.read())
                if all(k in decoded_body for k in props):
                 
                    try:
                        return HTTPResponse(status=200, body=manager.updateOne(id, decoded_body))              
                 
                    except NotFoundException as err:
                        return HTTPResponse(status=404, body={"error" : str(err)})
                    except Exception as err:
                        return HTTPResponse(status=500, body={"error" : err.args[0]})

                else:
                 return HTTPResponse(status=400, body={"error" : "The given json property doesn't contain all the neccesary properties." })
    except:
                return HTTPResponse(status=422, body={"error" : "The given course data is not a valid json obj." })
            


@delete('/courses/')
@delete('/courses/:id')
def delete_course(id=None):
     """Delete a Course by it's ID """
     if id is None:
      return HTTPResponse(status=400, body={"error" : "You must specify an ID for the given route." })
     try:
         return HTTPResponse(status=200, body=manager.deleteOne(id))
     except NotFoundException as err:
         return HTTPResponse(status=404, body={"error" : str(err) })
     except Exception as err:
         return HTTPResponse(status=500, body={"error" : err.args[0] })

       