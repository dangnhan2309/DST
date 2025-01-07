using OpenTK;
using OpenTK.Graphics;
using OpenTK.Graphics.OpenGL;
using OpenTK.Input;
using System;
using System.Collections.Generic;
public class Particle
{
    public Vector3 Position { get; private set; }
    public Vector3 Velocity { get; private set; }
    public Vector3 TargetPosition { get; private set; }
    public float Size { get; private set; }
    public Vector4 Color { get; private set; }

    public Particle(Vector3 position, Vector3 velocity, float size, Vector4 color)
    {
        Position = position;
        Velocity = velocity;
        TargetPosition = position;
        Size = size;
        Color = color;
    }

    public void SetTargetPosition(Vector3 target)
    {
        TargetPosition = target;
    }

    // Update particle's position towards the target position
    public void Update(float deltaTime)
    {
        // Calculate direction vector from the current position to the target position
        Vector3 direction = TargetPosition - Position;

        // Only move the particle if it's not already at the target position
        if (direction.Length > 0.01f) 
        {
            float speed = 0.5f; // You can adjust the speed here
            Position += direction.Normalized() * speed * deltaTime; // Move towards the target position
        }
    }

    public void Render()
    {
        GL.PointSize(Size * 40.0f); // Adjust particle size
        GL.Begin(PrimitiveType.Points);
        GL.Color4(Color);
        GL.Vertex3(Position);
        GL.End();
    }
}