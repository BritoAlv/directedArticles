# Business Rules and Use Cases

## Notes
Business rules are the rules or procedures related to our business. They are politics, or decisions related to the business, exist independently of the computer. They make the business win or save money, or solve the problem that the client has.

An entity is an object with contains business rules, but also the data that they may require. The entity, using that data, executes the business rules.

Ideally this should be separated from the concerns of our system. How the data is persisted, how is obtained, how the data is presented to the user, the entity should not be necessarily be a class, it could be a module with both objects and functions.  

The point is that following the single responsibility principle the business rules along with the data it depends on, should be separated from other concerns.

Not all the business rules are as pure as entities, some only makes sense in an automated environment. 

An use case is a description of the way an automated system is used. It specifies the input to be provided by the user, the output to be returned to the user, and the processing steps involved in producing that output. 

Use cases contain the rules that specify how and when the Critical Business Rules within the entities are invoked. 

The use case does not describe the user interface other than to informally specify the data coming in from that interface, and the data going back out through that interface.

From the use case, it is impossible to tell whether the application is delivered on the web, or on a tick client, or on a console.

Use cases do not describe how the system appears to the user, instead they describe the application-specific rules that govern the interaction between the users and the Entities. 

How the data gets in and out of the system is irrelevant to the use cases.

A use case is an object, it has one or more functions that implement application-specific business rules. It also has data elements that include the input data, the output data, and the references to the appropriate Entities with which it interacts. 

Entities have no knowledge of the use cases that controls them. This is an example of the Dependency Inversion Principle.

Entities are high level concepts, while use cases are lower level. The reason is that use cases are specific to an application while entities are more general.

The use case defines its input and its output, i.e. its interface.

Business rules are the reason a software system exists. They are the core functionality. They should be clean from the user interface or the database used and any other concern our system has. They are the heart of the system. The business rules should be the most independent and reusable code in the system.

## Single Responsibility Principle

SRP is about: together goes the things that share the same reason of change. The reason of change of this business rule is that the business needs to achieve something, not related on what interface the system provides the users to interact with or how that is persisted. That's why it should be separated from all of that, because its changes should not affect how the data is persisted. 

## Wikipedia Definitions Notes

Use cases are a technique for capturing, modeling, and specifying the requirements of a system. A use case corresponds to a set of behaviors that the system may perform in interaction with its actors, and which produces an observable result that contributes to its goals. Actors represent the role that human users or other systems have in the interaction.

Use cases are high level description of the flow that the automated system should follow. An example can be found here on the specification of the passkeys.

https://www.w3.org/TR/webauthn/#sctn-use-cases